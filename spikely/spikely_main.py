# Python imports
import sys
import pkg_resources
# PyQt imports
import PyQt5.QtGui as qg
import PyQt5.QtWidgets as qw
# spikely imports
from . import file_menu
from . import operation_view as sp_opv
from . import parameter_model as sp_pam
from . import parameter_view as sp_pav
from . import pipeline_model as sp_pim
from . import pipeline_view as sp_piv
from . import version


class SpikelyMainWindow(qw.QMainWindow):
    # Parent UI for application delegates to subwindow views/models
    def __init__(self):
        super().__init__()

        # Subwindows Views need underlying Model references
        self._parameter_model = sp_pam.ParameterModel()
        self._pipeline_model = sp_pim.PipelineModel(
            self._parameter_model)
        self._init_ui()

    def _init_ui(self):
        self.setWindowTitle("spikely")
        self.setGeometry(100, 100, 1152, 472)

        spikely_png_path = pkg_resources.resource_filename(
            'spikely.resources', 'spikely.png')

        self.setWindowIcon(qg.QIcon(spikely_png_path))
        self.statusBar().addPermanentWidget(
            qw.QLabel("Version " + version.__version__))

        menu_bar = self.menuBar()
        menu = file_menu.create_file_menu(self, self._pipeline_model)
        menu_bar.addMenu(menu)

        main_frame = qw.QFrame()
        self.setCentralWidget(main_frame)
        main_frame.setLayout(qw.QVBoxLayout())

        # Push subwindows down - create negative space below menu bar
        main_frame.layout().addStretch(1)

        pipe_param_splitter = qw.QSplitter()
        pipe_param_splitter.setChildrenCollapsible(False)

        # Subwindows for element pipeline and current element parameters
        pipe_param_splitter.addWidget(sp_piv.PipelineView(
            self._pipeline_model, self._parameter_model))
        pipe_param_splitter.addWidget(sp_pav.ParameterView(
            self._pipeline_model, self._parameter_model))
        pipe_param_splitter.setSizes([328, 640])
        main_frame.layout().addWidget(pipe_param_splitter)

        # Subwindow at bottom for pipeline operations (run, clear, queue)
        main_frame.layout().addWidget(sp_opv.OperationView(
            self._pipeline_model, self._parameter_model))


def launch_spikely():
    app = qw.QApplication(sys.argv)
    win = SpikelyMainWindow()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    launch_spikely()
