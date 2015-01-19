import os
import glob

from numpy import loadtxt

def findspark():
	
	sparkhome = os.getenv("SPARK_HOME")
	if sparkhome is None:
		raise Exception("The environment variable SPARK_HOME must be set to the Spark installation directory")
	else:
		return sparkhome

def findjar():
	
	calldir = os.path.dirname(os.path.realpath(__file__))
	jardir = os.path.join(calldir, '..', 'lib', '*.jar')
	jar = glob.glob(jardir)
	if len(jar) == 0 or not os.path.exists(jar[0]):
		raise Exception("Cannot find jar, looking at %s" % jar)
	else:
		return jar[0]

def loadrecent(filename, oldtime, oldoutput):

	try:
		fname = max(glob.iglob(filename), key=os.path.getctime)
	except:
		print('No file found')
		return [], oldtime

	newtime = os.path.getctime(fname)
	if not (newtime > oldtime):
		print('File is not new')
		return oldoutput, oldtime	

	try:
		f = open(fname)
		if os.fstat(f.fileno()).st_size == 0:
			print('File is empty')
			return [], oldtime

	except:
		print('Cannot load file')
		return [], oldtime

	prediction = loadtxt(fname, delimiter=',')
	return prediction, newtime

def baseargs(parser):

	parser.add_argument('path', type=str, 
		help='Temporary location to store outputs')
	parser.add_argument('-o', '--overwrite', type=bool, default=True, required=False,
		help='Whether to overwrite the temporary location if it already exists')
	parser.add_argument('-lgn', '--lightning', type=str, default=None, required=False,
		help='Lightning server for visualization')
	parser.add_argument('-bt', '--batchtime', type=int, default=1, required=False,
		help='Frequency of updates')
	parser.add_argument('-np', '--npoints', type=int, default=50, required=False,
		help='Number of data points per batch')
	parser.add_argument('-nb', '--nbatches', type=int, default=40, required=False,
		help='Number of batches')
	parser.add_argument('-hl', '--halflife', type=float, default=5, required=False,
		help='Half life for streaming updates')
	parser.add_argument('-tu', '--timeunit', type=str, default='batches', choices=('batches', 'points'), required=False, 
		help='Time unit for streaming updates')
	return parser