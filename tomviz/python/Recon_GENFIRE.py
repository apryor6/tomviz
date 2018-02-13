import genfire as gf
import tomviz.operators
import numpy as np

class ReconGENFIREOperator(tomviz.operators.CancelableOperator):
    def transform_scalars(self, dataset, **kwargs):

        # Get tilt angles
        from tomviz import utils
        tiltAngles = utils.get_tilt_angles(dataset)

        # Convert to Euler representation assuming single-tilt axis
        eulerAngles = np.zeros((len(tiltAngles), 3))
        eulerAngles[:, 1] = tiltAngles

        tiltSeries = utils.get_array(dataset)
        if tiltSeries is None:
            raise RuntimeError("No scalars found!")

        # Convert from Tomviz rotation axis convention to GENFIRE
        tiltSeries = np.roll(np.rot90(tiltSeries, k=1, axes=(0, 1)), shift=1, axis=0)

        # Convert enumerated type to that used by GENFIRE
        gridMap = {0:"FFT", 1:"DFT"}
        kwargs['griddingMethod'] = gridMap[kwargs['griddingMethod']]

        # Assemble rest of parameters
        pars = dict(
            projections = tiltSeries,
            eulerAngles = eulerAngles,
            resultsFilename = "recon.mrc",
            **kwargs
            )

        # Run the reconstruction
        GF = gf.reconstruct.GenfireReconstructor(**pars)
        results = GF.reconstruct()

        # Rotate volume back to match Tomviz orientation convention
        results['reconstruction'] = np.rot90(np.roll(results['reconstruction'], shift=-1, axis=0), k=3, axes=(0, 1))

        from vtk import vtkImageData
        recon_dataset = vtkImageData()
        recon_dataset.CopyStructure(dataset)
        utils.set_array(recon_dataset, np.asfortranarray(results['reconstruction']))
        utils.mark_as_volume(recon_dataset)
        return dict(reconstruction=recon_dataset)