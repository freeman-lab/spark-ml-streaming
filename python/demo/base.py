import os
import shutil


class StreamingDemo(object):

	def __init__(self, npoints=50, nbatches=5):
		self.npoints = npoints
		self.nbatches = nbatches

	def params(*args, **kwargs):
		""" Get analysis-specific parameters """
		raise NotImplementedError

	def run(*args, **kwargs):
		""" Run the streaming demo """
		raise NotImplementedError

	@staticmethod
	def make(demoname, *args, **kwargs):
		""" Create a streaming demo """

		from demo.kmeans import StreamingKMeans
		DEMOS = {
			'kmeans': StreamingKMeans
		}
		return DEMOS[demoname](*args, **kwargs)

	def setup(self, path, overwrite=False):
		""" Setup paths for a streaming demo where temporary data will be read / written"""

		if os.path.isdir(path):
			if overwrite:
				shutil.rmtree(path)
				os.mkdir(path)
			else:
				raise Exception('Base directory %s already exists and overwrite is set to False' % path)
		else:
			os.mkdir(path)

		datain = os.path.join(path, 'input')
		dataout = os.path.join(path, 'output')
		if os.path.isdir(datain):
			shutil.rmtree(datain)
		if os.path.isdir(dataout):
			shutil.rmtree(dataout)
		os.mkdir(datain)
		os.mkdir(dataout)
		self.datain = datain
		self.dataout = dataout
		return self

	def writepoints(self, pts, i):
		""" Write data points in a form that can be read by MLlib's vector parser  """

		f = file(os.path.join(self.datain, 'batch%g.txt' % i), 'w')
		s = map(lambda p: ",".join(str(p).split()).replace('[,','[').replace(',]',']'), pts)
		tmp = "\n".join(s)
		f.write(tmp)
		f.close()

