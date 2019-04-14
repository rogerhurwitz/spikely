"""Creates an MVC view-control for constructing the active pipeline model.

The Construct Pipeline view/control consists of widgets responsible for
constructing the active pipeline by inserting, deleting, or moving elements
within the active pipeline.
"""

import sys
import PyQt5.QtWidgets as qw
import PyQt5.QtGui as qg
import PyQt5.QtCore as qc

from pi_model import SpikePipeline
from el_model import SpikeElement
import spikely_constants as sc


class ConstructPipelineView(qw.QGroupBox):
    """GroupBox of widgets capable of constructing active pipeline.

    No public methods other than constructor.  All other activites
    of object are triggered by user interaction with sub widgets.
    """

    def __init__(self, active_pipe):
        """Initialize parent and member variables, construct UI."""
        super().__init__("Construct Pipeline")
        self._active_pipe = active_pipe
        self._ele_cbx = qw.QComboBox()
        self._ele_cbx.setEditable(False)
        self._init_ui()

    def _stage_changed(self, index):
        """Slot for currentIndexChanged signal from stage cbox."""
        # elements = SpikeElement.avail_elements(index)
        self._ele_cbx.clear()
        for element in SpikeElement.avail_elements(index):
            self._ele_cbx.addItem(element.name(), element)

    def _add_element(self):
        """Slot for add button clicked signal."""
        # print(self._ele_cbx.currentData().name())
        self._active_pipe.add_element(self._ele_cbx.currentData())

    def _init_ui(self):
        """Build composite UI for region.

        Region consists of Controllers for adding and maninpulating active
        pipeline elements and a View of the in-construction active pipeline.
        """
        # Lay out controllers and view from top to bottom of group box
        cp_layout = qw.QVBoxLayout()
        self.setLayout(cp_layout)

        # Selection: Lay out view-controllers in frame from left to right
        sel_layout = qw.QHBoxLayout()
        sel_frame = qw.QFrame()
        sel_frame.setLayout(sel_layout)

        stage_cbx = qw.QComboBox()
        stage_cbx.currentIndexChanged.connect(self._stage_changed)
        for stage in sc.STAGE_NAMES:
            stage_cbx.addItem(stage)
        sel_layout.addWidget(stage_cbx)

        # self._ele_cbx = qw.QComboBox()
        sel_layout.addWidget(self._ele_cbx)

        add_button = qw.QPushButton("Add Element")
        add_button.setToolTip("Push to add element to pipeline.")
        add_button.clicked.connect(self._add_element)
        sel_layout.addWidget(add_button)
        cp_layout.addWidget(sel_frame)

        # Display: Hierarchical (Tree) view of in-construction pipeline

        self.pipe_view = qw.QListView(self)
        self.pipe_view.setModel(self._active_pipe)
        cp_layout.addWidget(self.pipe_view)

        """This funky bit of code is an example of how a class method
        with a specific signature can be bound to an instance of that class
        using a type index, in this case QModelIndex"""
        # treeView.clicked[QModelIndex].connect(self.clicked)

        # Manipulation: Control buttons ordered lef to right
        man_layout = qw.QHBoxLayout()
        man_frame = qw.QFrame()
        # man_frame.setEnabled(False)
        man_frame.setLayout(man_layout)

        for lbl in ["Move Up", "Delete", "Move Down"]:
            btn = qw.QPushButton(lbl)
            man_layout.addWidget(btn)

        cp_layout.addWidget(man_frame)
