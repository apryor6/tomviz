/******************************************************************************

  This source file is part of the tomviz project.

  Copyright Kitware, Inc.

  This source code is released under the New BSD License, (the "License").

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.

******************************************************************************/
#ifndef tomvizModuleVolumeWidget_h
#define tomvizModuleVolumeWidget_h

#include <QScopedPointer>
#include <QWidget>

/**
 * \brief UI layer of ModuleVolume.
 *
 * Signals are forwarded to the actuators on the mapper in ModuleVolume.
 * This class is intended to contain only logic related to UI actions.
 */

namespace Ui {
class ModuleVolumeWidget;
class LightingParametersForm;
}

namespace tomviz {

class ModuleVolumeWidget : public QWidget
{
  Q_OBJECT

public:
  ModuleVolumeWidget(QWidget* parent_ = nullptr);
  ~ModuleVolumeWidget() override;

  //@{
  /**
   * UI update methods. The actual model state is stored in ModelVolume (either
   * in the mapper or serialized), so the UI needs to be updated if the state
   * changes or when constructing the UI.
   */
  void setJittering(const bool enable);
  void setBlendingMode(const int mode);
  void setInterpolationType(const int type);
  void setLighting(const bool enable);
  void setAmbient(const double value);
  void setDiffuse(const double value);
  void setSpecular(const double value);
  void setSpecularPower(const double value);
  void setTransferMode(const int transferMode);
  //@}

signals:
  //@{
  /**
   * Forwarded signals.
   */
  void jitteringToggled(const bool state);
  void blendingChanged(const int state);
  void interpolationChanged(const int state);
  void lightingToggled(const bool state);
  void ambientChanged(const double value);
  void diffuseChanged(const double value);
  void specularChanged(const double value);
  void specularPowerChanged(const double value);
  void transferModeChanged(const int mode);
  //@}

private:
  ModuleVolumeWidget(const ModuleVolumeWidget&) = delete;
  void operator=(const ModuleVolumeWidget&) = delete;

  bool usesLighting(const int mode) const;

  QScopedPointer<Ui::ModuleVolumeWidget> m_ui;
  QScopedPointer<Ui::LightingParametersForm> m_uiLighting;

private slots:
  void onBlendingChanged(const int mode);
};
}
#endif
