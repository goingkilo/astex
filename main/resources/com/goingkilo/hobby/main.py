print 'hisssss'


from  java.io  import BufferedReader,File,FileReader,IOException;
from java.util import  HashSet,Set;
from java.lang import String;

from  org.eclipse.jdt.core.dom import AST,ASTParser,ASTVisitor,CompilationUnit,SimpleName,VariableDeclarationFragment;
 
 
def parse( program):
    parser = ASTParser.newParser(AST.JLS3);
    parser.setSource( String(program).toCharArray());
    parser.setKind(ASTParser.K_COMPILATION_UNIT);
    
    cu = parser.createAST(None);
    print cu
    
    
    
    
parse( open('/Users/kraghunathan/myrepos/kong/src/main/java/com/goingkilo/web/GeneralResource.java').read()  )
print 'ssssslither'