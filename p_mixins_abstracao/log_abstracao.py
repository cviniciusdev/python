class Log:
    def log(self, msg):
        raise NotImplementedError('Implemten o método log')
    
class LogFileMixin(Log):

    
if __name__== 'main':    
    l = Log()
    l.log('qualquer coisa')
    
