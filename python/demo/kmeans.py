import time
import shutil
import os
import glob

from numpy import asarray, loadtxt, vstack, hstack, size, random
from sklearn.datasets import make_blobs

from demo.base import StreamingDemo

class StreamingKMeans(StreamingDemo):

	def params(self, ncenters=3, ndims=2, std=0.2, seed=None):

		random.seed(seed)
		centers = random.randn(ncenters, ndims)
		self.centers = asarray(centers)
		self.ncenters = ncenters
		self.ndims = ndims
		self.std = std
		return self

	def run(self, lgn=None):

		viz = None
		
		for i in range(0, self.nbatches):
			
			print('running batch %g' % i)

			centers = self.centers.copy()
			npoints = self.npoints
			pts, clrs = make_blobs(npoints, self.ndims, centers, cluster_std=self.std)
			self.writepoints(pts, i)
			time.sleep(1)

			# try:
			output = glob.iglob(self.dataout + '/*')
			try:
				fname = max(output, key=os.path.getctime)
				result = loadtxt(fname, delimiter=',')
			 	pts = vstack((pts, result))
			 	clrs = hstack((clrs, [3,4,5]))
			except:
			 	print('no outputs yet')

			if lgn:
				if viz is None:
 		 			viz = lgn.scatterstreaming(pts[:,0], pts[:,1], label=clrs)
				else:
 					viz.append(pts[:,0], pts[:,1], label=clrs)
