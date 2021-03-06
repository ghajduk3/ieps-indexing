from .InvertedIndex import InvertedIndex
from .SequentialIndex import SequantialIndex


class IndexFactory:
    @staticmethod
    def getIndexByType(indexType, inputPath, outputPath, forceRecreate):
        if indexType == "inverted":
            return InvertedIndex(inputPath, outputPath, forceRecreate)
        elif indexType == "sequential":
            return SequantialIndex(inputPath, outputPath, forceRecreate)
        else:
            raise Exception("Unknown index type")
