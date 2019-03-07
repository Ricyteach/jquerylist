from random import randint

import ipywidgets.widgets as widgets
from traitlets import Unicode, Dict


class JQueryList(widgets.DOMWidget):
    pass


'''
# Pythonified version of javascript code.... 

class Element:
    def html(self, text):
        pass

    def find(self, query):
        yield from (Element() for _ in range(10))

    def querySelectorAll(self, query):
        yield from (Element() for _ in range(10))

    def click(self, func):
        pass

    @property
    def classList(self):
        return []

    def val(self):
        return ""

    def addEventListener(self, name, func):
        pass

    def innerHTML(self, html):
        pass


document = Element()


class Collection:
    def __init__(self, name, selections):
        self.name = name
        self.selections = selections


class Console:
    def log(self, *msgs):
        print(*msgs)


console = Console()
alert = console.log


class JQueryView(jupyter_widgets.base.DOMWidgetView):

    @property
    def element(self):
        return Element()

    @property
    def model(self):
        return getmodel(self)

    def render(self):
        self.element.innerHTML(self.model.get('html'))

    def __init__(self):

        # Mutable collection data to send back up the wire "somehow"
        self.collection = Collection(name = '', selections = [])

        # Each path element is a polygon const
        polygons = self.element.find('#polygonGeometry path')

        def click_polygon(idx, p):
            try:
                self.remove(idx, p)
            except ValueError:
                self.add(idx, p)

        # Add click event to polygons
        for idx,p in enumerate(polygons, start=1):
            p.addEventListener('click', lambda: click_polygon(idx, p))
            console.log('path #', idx, ' click set')

        # Attach functions to buttons
        next(self.element.find('#clearBtn')).click(self.clear)
        console.log('clearBtn action set')
        next(self.element.find('#saveBtn')).click(self.save)
        console.log('saveBtn action set')

    # Add item to selection list
    def add(self, idx, p):
        p.classList.append('selectedPolygon')
        console.log('path #', idx, ' added')
        self.collection.selections.push(idx)
        console.log('pushed #', idx)

    # Remove item from selection list
    def remove(self, idx, p):
        p.classList.remove('selectedPolygon')
        console.log('path #', idx, ' removed')
        self.collection.selections.remove(idx)
        console.log('filtered #', idx)

    # Remove all items
    def clear(self):
        console.log('clear() clicked')
        self.collection.selections = []
        for path in document.querySelectorAll('.selectedPolygon'):
            path.classList.remove('selectedPolygon')
        console.log('Data cleared')

    # Set collection name and send current selection back up - wire
    def save(self):
        console.log('save() clicked')
        nameInput = next(self.element.find('#name'))
        if (not nameInput.val() or self.collection.selections.length < 1):
            alert('Collections must have a name and selected polygons')
        else:
            self.collection.name = nameInput.val()
        console.log('You saved some data')
        console.log("Selection Name: ", self.collection.name)
        console.log(self.collection.selections)


def getmodel(view):
    return {view: "the model value"}
'''