gui_params = [
    {
        "name": "output_folder",
        "type": "folder",
        "value": None,
        "default": None,
        "title": "Sorting output folder path.",
        "base_param": True,
    },
    {
        "name": "verbose",
        "type": "bool",
        "value": False,
        "default": False,
        "title": "If True, output from SpikeInterface element is verbose when run.",
        "base_param": True,
    },
    {
        "name": "grouping_property",
        "type": "str",
        "value": None,
        "default": None,
        "title": "Property name to be used for sorter output grouping.",
        "base_param": True,
    },
    {
        "name": "parallel",
        "type": "bool",
        "value": False,
        "default": False,
        "title": "If grouping property specifed, sort property groups in parallel if True.",
        "base_param": True,
    },
    {
        "name": "delete_output_folder",
        "type": "bool",
        "value": False,
        "default": False,
        "title": "Delete specified or default output folder on completion if True.",
        "base_param": True,
    },
    # Klusta specific parameters
    {
        "name": "adjacency_radius",
        "type": "float",
        "value": None,
        "default": None,
        "title": "Adjacency radius (microns).",
    },
    {
        "name": "threshold_strong_std_factor",
        "type": "int",
        "value": 5,
        "default": 5,
        "title": "Threshold strong std factor.",
    },
    {
        "name": "threshold_weak_std_factor",
        "type": "int",
        "value": 2,
        "default": 2,
        "title": "Threshold weak std factor.",
    },
    {
        "name": "detect_sign",
        "type": "int",
        "value": -1,
        "default": -1,
        "title": "Use -1, 0, or 1, depending on the sign of the spikes in the recording.",
    },
    {
        "name": "extract_s_before",
        "type": "int",
        "value": 16,
        "default": 16,
        "title": "Frames to extract before.",
    },
    {
        "name": "extract_s_after",
        "type": "int",
        "value": 32,
        "default": 32,
        "title": "Frames to extract after.",
    },
    {
        "name": "n_features_per_channel",
        "type": "int",
        "value": 3,
        "default": 3,
        "title": "Number of features per channel.",
    },
    {
        "name": "pca_n_waveforms_max",
        "type": "int",
        "value": 10_000,
        "default": 10_000,
        "title": "Max number of waveforms for PCA.",
    },
    {
        "name": "num_starting_clusters",
        "type": "int",
        "value": 50,
        "default": 50,
        "title": "Starting number of clusters.",
    },
]
