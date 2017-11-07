import genfire as gf
import tomviz.operators

class ReconGENFIREOperator(tomviz.operators.CancelableOperator):
    def transform_scalars(self, Niter=50, OversamplingRatio=3, GriddingMethod="FFT", ResolutionExSupp=1,
     InterpolationCutoffDistance=0.5):
        print("GENFIRE transform_scalars invoked")
        # Get Tilt angles
        tilt_angles = utils.get_tilt_angles(dataset)

        tiltSeries = utils.get_array(dataset)
        if tiltSeries is None:
            raise RuntimeError("No scalars found!")
        Nslice = tiltSeries.shape[0]
        print("TiltAngles = {}".format(tilt_angles))
        print("Nslice = {}".format(Nslice))
