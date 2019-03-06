import ipywidgets.widgets as widgets
from traitlets import Unicode, List


class JQueryList(widgets.DOMWidget):
    _view_name = Unicode('JQueryListView').tag(sync=True)
    _view_module = Unicode('jquerylist').tag(sync=True)
    seq = List([1,2,3]).tag(sync=True)
