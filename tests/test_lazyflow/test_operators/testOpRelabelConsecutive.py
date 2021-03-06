from builtins import object
import numpy as np
import pytest
import vigra
from lazyflow.graph import Graph
from lazyflow.operators import OpRelabelConsecutive

pandas = pytest.importorskip("pandas")


class TestOpRelabelConsecutive(object):
    def test_simple(self):
        op = OpRelabelConsecutive(graph=Graph())

        labels = 2 * np.arange(0, 100, dtype=np.uint8).reshape((10, 10))
        labels = vigra.taggedView(labels, "yx")
        op.Input.setValue(labels)
        relabeled = op.Output[:].wait()
        assert (relabeled == labels // 2).all()

    def test_startlabel(self):
        op = OpRelabelConsecutive(graph=Graph())
        op.StartLabel.setValue(10)

        labels = 2 * np.arange(0, 100, dtype=np.uint8).reshape((10, 10))
        labels = vigra.taggedView(labels, "yx")
        op.Input.setValue(labels)
        relabeled = op.Output[:].wait()
        assert (relabeled == 10 + labels // 2).all()
