import sys 
import os 
import pyodbc 
  
from argparse import ArgumentParser 
from argparse import RawDescriptionHelpFormatter 
  
__all__ = [] 
__version__ = 0.2 
__date__ = '2019-10-07' 
__updated__ = '2019-10-07' 
  
DEBUG = 1 
TESTRUN = 0 
PROFILE = 0 
  
class CLIError(Exception): 
    '''Generic exception to raise and log different fatal errors.''' 
    def __init__(self, msg): 
        super(CLIError).__init__(type(self)) 
        self.msg = "E: %s" % msg 
    def __str__(self): 
        return self.msg 
    def __unicode__(self): 
        return self.msg 
  
def main(argv=None): # IGNORE:C0111 
    '''Command line options.''' 
  
    if argv is None: 
        argv = sys.argv 
    else: 
        sys.argv.extend(argv) 
  
    program_name = os.path.basename(sys.argv[0]) 
    program_version = "v%s" % __version__ 
    program_build_date = str(__updated__) 
    program_version_message = '%%(prog)s %s (%s)' % (program_version, program_build_date) 
    program_shortdesc = __import__('__main__').__doc__.split("n")[1] 
    program_license = '''%s
    
    
    ''' % (program_shortdesc, str(__date__)) 
  
    try: 
        # Setup argument parser 
        parser = ArgumentParser(description=program_license, formatter_class=RawDescriptionHelpFormatter) 
        parser.add_argument('connstr')         
        parser.add_argument('query') 
         
        # Process arguments 
        args = parser.parse_args() 
  
        query = args.query 
        connstr = args.connstr 
  
        conn = pyodbc.connect(connstr) 
        cursor = conn.cursor() 
        cursor.execute(query) 
        while 1: 
            row = None 
            try: 
                row = cursor.fetchone() 
            except:  
                print(sys.exc_info()[1]) 
                break 
            if not row: 
                break                     
            print(row) 
                         
             
    except KeyboardInterrupt: 
        ### handle keyboard interrupt ### 
        return 0 
    except: 
        print(sys.exc_info()[1]) 
        #indent = len(program_name) * " "         
        #sys.stderr.write(program_name + ": " + repr(e) + "n") 
        #sys.stderr.write(indent + "  for help use --help") 
        return 2 
  
if __name__ == "__main__": 
          
    if TESTRUN: 
        import doctest 
        doctest.testmod() 
    if PROFILE: 
        import cProfile 
        import pstats 
        profile_filename = 'CBQuery_profile.txt' 
        cProfile.run('main()', profile_filename) 
        statsfile = open("profile_stats.txt", "wb") 
        p = pstats.Stats(profile_filename, stream=statsfile) 
        stats = p.strip_dirs().sort_stats('cumulative') 
        stats.print_stats() 
        statsfile.close() 
        sys.exit(0) 
    sys.exit(main())