import platform

if platform.system() == 'Windows':
    EXECUTION_SUFFIX = '.exe'
elif platform.system() == 'Linux':
    EXECUTION_SUFFIX = ''
else:
    EXECUTION_SUFFIX = ''
