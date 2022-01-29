# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2C")
        buf.write("\u0245\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\3\2")
        buf.write("\3\2\5\2\u009a\n\2\3\2\7\2\u009d\n\2\f\2\16\2\u00a0\13")
        buf.write("\2\3\3\3\3\3\3\3\3\5\3\u00a6\n\3\3\3\7\3\u00a9\n\3\f\3")
        buf.write("\16\3\u00ac\13\3\3\4\3\4\3\4\5\4\u00b1\n\4\3\4\7\4\u00b4")
        buf.write("\n\4\f\4\16\4\u00b7\13\4\3\5\3\5\3\5\3\5\5\5\u00bd\n\5")
        buf.write("\3\5\7\5\u00c0\n\5\f\5\16\5\u00c3\13\5\3\6\3\6\3\6\3\6")
        buf.write("\5\6\u00c9\n\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\5\7\u00da\n\7\3\7\3\7\3\b\3\b\5\b")
        buf.write("\u00e0\n\b\3\b\6\b\u00e3\n\b\r\b\16\b\u00e4\3\t\3\t\7")
        buf.write("\t\u00e9\n\t\f\t\16\t\u00ec\13\t\3\n\3\n\5\n\u00f0\n\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\5\n\u00f7\n\n\3\n\3\n\3\n\5\n\u00fc")
        buf.write("\n\n\3\n\3\n\3\n\3\n\5\n\u0102\n\n\3\n\3\n\3\13\3\13\5")
        buf.write("\13\u0108\n\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\5\f\u0118\n\f\3\r\3\r\3\r\5\r\u011d\n")
        buf.write("\r\3\16\3\16\5\16\u0121\n\16\3\17\3\17\3\17\3\17\7\17")
        buf.write("\u0127\n\17\f\17\16\17\u012a\13\17\3\17\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25")
        buf.write("\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3!\3")
        buf.write("!\3!\3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3#\3$\3$\3$\3$\3$\3")
        buf.write("$\3%\3%\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3&\3\'\3\'")
        buf.write("\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3)")
        buf.write("\3*\3*\3*\3*\3*\3+\3+\3+\3+\3,\3,\3,\3,\3-\3-\3-\3-\3")
        buf.write("-\3-\3-\3-\3-\3-\3-\3-\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3")
        buf.write(".\3/\3/\3/\3/\3\60\3\60\3\60\3\61\3\61\3\62\3\62\3\63")
        buf.write("\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\3\67\38")
        buf.write("\38\38\39\39\39\3:\3:\3;\3;\3;\3<\3<\3=\3=\3>\3>\3>\3")
        buf.write("?\3?\3?\3@\3@\3@\3@\3A\3A\3A\3B\3B\3B\3C\3C\3D\3D\3D\3")
        buf.write("E\3E\7E\u0207\nE\fE\16E\u020a\13E\3F\3F\6F\u020e\nF\r")
        buf.write("F\16F\u020f\3G\3G\3G\3G\7G\u0216\nG\fG\16G\u0219\13G\3")
        buf.write("G\3G\3G\3G\3G\3H\6H\u0221\nH\rH\16H\u0222\3H\3H\3I\3I")
        buf.write("\3I\7I\u022a\nI\fI\16I\u022d\13I\3I\5I\u0230\nI\3I\3I")
        buf.write("\3J\3J\3J\3J\7J\u0238\nJ\fJ\16J\u023b\13J\3J\3J\5J\u023f")
        buf.write("\nJ\3J\3J\3K\3K\3K\3\u0217\2L\3\2\5\2\7\2\t\2\13\3\r\4")
        buf.write("\17\2\21\2\23\5\25\6\27\2\31\2\33\2\35\7\37\b!\t#\n%\13")
        buf.write("\'\f)\r+\16-\17/\20\61\21\63\22\65\23\67\249\25;\26=\27")
        buf.write("?\30A\31C\32E\33G\34I\35K\36M\37O Q!S\"U#W$Y%[&]\'_(a")
        buf.write(")c*e+g,i-k.m/o\60q\61s\62u\63w\64y\65{\66}\67\1778\u0081")
        buf.write("9\u0083:\u0085;\u0087<\u0089=\u008b>\u008d?\u008f@\u0091")
        buf.write("A\u0093B\u0095C\3\2\25\3\2\63;\3\2\62;\4\2DDdd\3\2\62")
        buf.write("\63\3\2\639\3\2\629\4\2ZZzz\4\2\63;CH\4\2\62;CH\4\2GG")
        buf.write("gg\4\2--//\3\2))\n\2$$))^^ddhhppttvv\6\2\n\f\16\17$$^")
        buf.write("^\3\2$$\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\17\17\"\"\4")
        buf.write("\3\f\f\16\17\2\u026a\2\13\3\2\2\2\2\r\3\2\2\2\2\23\3\2")
        buf.write("\2\2\2\25\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2")
        buf.write("\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2")
        buf.write("\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3")
        buf.write("\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e")
        buf.write("\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2")
        buf.write("o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2")
        buf.write("\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081")
        buf.write("\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2")
        buf.write("\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f")
        buf.write("\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2")
        buf.write("\2\3\u0097\3\2\2\2\5\u00a1\3\2\2\2\7\u00ad\3\2\2\2\t\u00b8")
        buf.write("\3\2\2\2\13\u00c8\3\2\2\2\r\u00d9\3\2\2\2\17\u00dd\3\2")
        buf.write("\2\2\21\u00e6\3\2\2\2\23\u0101\3\2\2\2\25\u0107\3\2\2")
        buf.write("\2\27\u0117\3\2\2\2\31\u011c\3\2\2\2\33\u0120\3\2\2\2")
        buf.write("\35\u0122\3\2\2\2\37\u012f\3\2\2\2!\u0131\3\2\2\2#\u0133")
        buf.write("\3\2\2\2%\u0135\3\2\2\2\'\u0137\3\2\2\2)\u0139\3\2\2\2")
        buf.write("+\u013b\3\2\2\2-\u013d\3\2\2\2/\u013f\3\2\2\2\61\u0141")
        buf.write("\3\2\2\2\63\u0147\3\2\2\2\65\u0150\3\2\2\2\67\u0153\3")
        buf.write("\2\2\29\u015a\3\2\2\2;\u015f\3\2\2\2=\u0167\3\2\2\2?\u016c")
        buf.write("\3\2\2\2A\u0172\3\2\2\2C\u0178\3\2\2\2E\u017b\3\2\2\2")
        buf.write("G\u017f\3\2\2\2I\u0185\3\2\2\2K\u018d\3\2\2\2M\u0194\3")
        buf.write("\2\2\2O\u019b\3\2\2\2Q\u01a0\3\2\2\2S\u01a6\3\2\2\2U\u01ab")
        buf.write("\3\2\2\2W\u01af\3\2\2\2Y\u01b3\3\2\2\2[\u01bf\3\2\2\2")
        buf.write("]\u01ca\3\2\2\2_\u01ce\3\2\2\2a\u01d1\3\2\2\2c\u01d3\3")
        buf.write("\2\2\2e\u01d5\3\2\2\2g\u01d7\3\2\2\2i\u01d9\3\2\2\2k\u01db")
        buf.write("\3\2\2\2m\u01dd\3\2\2\2o\u01e0\3\2\2\2q\u01e3\3\2\2\2")
        buf.write("s\u01e6\3\2\2\2u\u01e8\3\2\2\2w\u01eb\3\2\2\2y\u01ed\3")
        buf.write("\2\2\2{\u01ef\3\2\2\2}\u01f2\3\2\2\2\177\u01f5\3\2\2\2")
        buf.write("\u0081\u01f9\3\2\2\2\u0083\u01fc\3\2\2\2\u0085\u01ff\3")
        buf.write("\2\2\2\u0087\u0201\3\2\2\2\u0089\u0204\3\2\2\2\u008b\u020b")
        buf.write("\3\2\2\2\u008d\u0211\3\2\2\2\u008f\u0220\3\2\2\2\u0091")
        buf.write("\u0226\3\2\2\2\u0093\u0233\3\2\2\2\u0095\u0242\3\2\2\2")
        buf.write("\u0097\u009e\t\2\2\2\u0098\u009a\7a\2\2\u0099\u0098\3")
        buf.write("\2\2\2\u0099\u009a\3\2\2\2\u009a\u009b\3\2\2\2\u009b\u009d")
        buf.write("\t\3\2\2\u009c\u0099\3\2\2\2\u009d\u00a0\3\2\2\2\u009e")
        buf.write("\u009c\3\2\2\2\u009e\u009f\3\2\2\2\u009f\4\3\2\2\2\u00a0")
        buf.write("\u009e\3\2\2\2\u00a1\u00a2\7\62\2\2\u00a2\u00a3\t\4\2")
        buf.write("\2\u00a3\u00aa\7\63\2\2\u00a4\u00a6\7a\2\2\u00a5\u00a4")
        buf.write("\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7")
        buf.write("\u00a9\t\5\2\2\u00a8\u00a5\3\2\2\2\u00a9\u00ac\3\2\2\2")
        buf.write("\u00aa\u00a8\3\2\2\2\u00aa\u00ab\3\2\2\2\u00ab\6\3\2\2")
        buf.write("\2\u00ac\u00aa\3\2\2\2\u00ad\u00ae\7\62\2\2\u00ae\u00b5")
        buf.write("\t\6\2\2\u00af\u00b1\7a\2\2\u00b0\u00af\3\2\2\2\u00b0")
        buf.write("\u00b1\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\u00b4\t\7\2\2")
        buf.write("\u00b3\u00b0\3\2\2\2\u00b4\u00b7\3\2\2\2\u00b5\u00b3\3")
        buf.write("\2\2\2\u00b5\u00b6\3\2\2\2\u00b6\b\3\2\2\2\u00b7\u00b5")
        buf.write("\3\2\2\2\u00b8\u00b9\7\62\2\2\u00b9\u00ba\t\b\2\2\u00ba")
        buf.write("\u00c1\t\t\2\2\u00bb\u00bd\7a\2\2\u00bc\u00bb\3\2\2\2")
        buf.write("\u00bc\u00bd\3\2\2\2\u00bd\u00be\3\2\2\2\u00be\u00c0\t")
        buf.write("\n\2\2\u00bf\u00bc\3\2\2\2\u00c0\u00c3\3\2\2\2\u00c1\u00bf")
        buf.write("\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2\n\3\2\2\2\u00c3\u00c1")
        buf.write("\3\2\2\2\u00c4\u00c9\5\3\2\2\u00c5\u00c9\5\5\3\2\u00c6")
        buf.write("\u00c9\5\7\4\2\u00c7\u00c9\5\t\5\2\u00c8\u00c4\3\2\2\2")
        buf.write("\u00c8\u00c5\3\2\2\2\u00c8\u00c6\3\2\2\2\u00c8\u00c7\3")
        buf.write("\2\2\2\u00c9\u00ca\3\2\2\2\u00ca\u00cb\b\6\2\2\u00cb\f")
        buf.write("\3\2\2\2\u00cc\u00da\5\3\2\2\u00cd\u00da\5\5\3\2\u00ce")
        buf.write("\u00da\5\7\4\2\u00cf\u00da\5\t\5\2\u00d0\u00da\7\62\2")
        buf.write("\2\u00d1\u00d2\7\62\2\2\u00d2\u00d3\t\b\2\2\u00d3\u00da")
        buf.write("\7\62\2\2\u00d4\u00d5\7\62\2\2\u00d5\u00d6\t\4\2\2\u00d6")
        buf.write("\u00da\7\62\2\2\u00d7\u00d8\7\62\2\2\u00d8\u00da\7\62")
        buf.write("\2\2\u00d9\u00cc\3\2\2\2\u00d9\u00cd\3\2\2\2\u00d9\u00ce")
        buf.write("\3\2\2\2\u00d9\u00cf\3\2\2\2\u00d9\u00d0\3\2\2\2\u00d9")
        buf.write("\u00d1\3\2\2\2\u00d9\u00d4\3\2\2\2\u00d9\u00d7\3\2\2\2")
        buf.write("\u00da\u00db\3\2\2\2\u00db\u00dc\b\7\3\2\u00dc\16\3\2")
        buf.write("\2\2\u00dd\u00df\t\13\2\2\u00de\u00e0\t\f\2\2\u00df\u00de")
        buf.write("\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0\u00e2\3\2\2\2\u00e1")
        buf.write("\u00e3\t\3\2\2\u00e2\u00e1\3\2\2\2\u00e3\u00e4\3\2\2\2")
        buf.write("\u00e4\u00e2\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5\20\3\2")
        buf.write("\2\2\u00e6\u00ea\7\60\2\2\u00e7\u00e9\t\3\2\2\u00e8\u00e7")
        buf.write("\3\2\2\2\u00e9\u00ec\3\2\2\2\u00ea\u00e8\3\2\2\2\u00ea")
        buf.write("\u00eb\3\2\2\2\u00eb\22\3\2\2\2\u00ec\u00ea\3\2\2\2\u00ed")
        buf.write("\u00f0\5\3\2\2\u00ee\u00f0\7\62\2\2\u00ef\u00ed\3\2\2")
        buf.write("\2\u00ef\u00ee\3\2\2\2\u00f0\u00f1\3\2\2\2\u00f1\u00f2")
        buf.write("\5\21\t\2\u00f2\u00f3\5\17\b\2\u00f3\u0102\3\2\2\2\u00f4")
        buf.write("\u00f7\5\3\2\2\u00f5\u00f7\7\62\2\2\u00f6\u00f4\3\2\2")
        buf.write("\2\u00f6\u00f5\3\2\2\2\u00f7\u00f8\3\2\2\2\u00f8\u0102")
        buf.write("\5\21\t\2\u00f9\u00fc\5\3\2\2\u00fa\u00fc\7\62\2\2\u00fb")
        buf.write("\u00f9\3\2\2\2\u00fb\u00fa\3\2\2\2\u00fc\u00fd\3\2\2\2")
        buf.write("\u00fd\u0102\5\17\b\2\u00fe\u00ff\5\21\t\2\u00ff\u0100")
        buf.write("\5\17\b\2\u0100\u0102\3\2\2\2\u0101\u00ef\3\2\2\2\u0101")
        buf.write("\u00f6\3\2\2\2\u0101\u00fb\3\2\2\2\u0101\u00fe\3\2\2\2")
        buf.write("\u0102\u0103\3\2\2\2\u0103\u0104\b\n\4\2\u0104\24\3\2")
        buf.write("\2\2\u0105\u0108\5=\37\2\u0106\u0108\5? \2\u0107\u0105")
        buf.write("\3\2\2\2\u0107\u0106\3\2\2\2\u0108\26\3\2\2\2\u0109\u010a")
        buf.write("\7^\2\2\u010a\u0118\7d\2\2\u010b\u010c\7^\2\2\u010c\u0118")
        buf.write("\7h\2\2\u010d\u010e\7^\2\2\u010e\u0118\7p\2\2\u010f\u0110")
        buf.write("\7^\2\2\u0110\u0118\7t\2\2\u0111\u0112\7^\2\2\u0112\u0118")
        buf.write("\7v\2\2\u0113\u0114\7^\2\2\u0114\u0118\7^\2\2\u0115\u0116")
        buf.write("\7^\2\2\u0116\u0118\t\r\2\2\u0117\u0109\3\2\2\2\u0117")
        buf.write("\u010b\3\2\2\2\u0117\u010d\3\2\2\2\u0117\u010f\3\2\2\2")
        buf.write("\u0117\u0111\3\2\2\2\u0117\u0113\3\2\2\2\u0117\u0115\3")
        buf.write("\2\2\2\u0118\30\3\2\2\2\u0119\u011a\7^\2\2\u011a\u011d")
        buf.write("\n\16\2\2\u011b\u011d\7^\2\2\u011c\u0119\3\2\2\2\u011c")
        buf.write("\u011b\3\2\2\2\u011d\32\3\2\2\2\u011e\u0121\n\17\2\2\u011f")
        buf.write("\u0121\5\27\f\2\u0120\u011e\3\2\2\2\u0120\u011f\3\2\2")
        buf.write("\2\u0121\34\3\2\2\2\u0122\u0128\t\20\2\2\u0123\u0127\5")
        buf.write("\33\16\2\u0124\u0125\t\r\2\2\u0125\u0127\t\20\2\2\u0126")
        buf.write("\u0123\3\2\2\2\u0126\u0124\3\2\2\2\u0127\u012a\3\2\2\2")
        buf.write("\u0128\u0126\3\2\2\2\u0128\u0129\3\2\2\2\u0129\u012b\3")
        buf.write("\2\2\2\u012a\u0128\3\2\2\2\u012b\u012c\t\20\2\2\u012c")
        buf.write("\u012d\3\2\2\2\u012d\u012e\b\17\5\2\u012e\36\3\2\2\2\u012f")
        buf.write("\u0130\7*\2\2\u0130 \3\2\2\2\u0131\u0132\7+\2\2\u0132")
        buf.write("\"\3\2\2\2\u0133\u0134\7}\2\2\u0134$\3\2\2\2\u0135\u0136")
        buf.write("\7\177\2\2\u0136&\3\2\2\2\u0137\u0138\7]\2\2\u0138(\3")
        buf.write("\2\2\2\u0139\u013a\7_\2\2\u013a*\3\2\2\2\u013b\u013c\7")
        buf.write("<\2\2\u013c,\3\2\2\2\u013d\u013e\7=\2\2\u013e.\3\2\2\2")
        buf.write("\u013f\u0140\7.\2\2\u0140\60\3\2\2\2\u0141\u0142\7D\2")
        buf.write("\2\u0142\u0143\7t\2\2\u0143\u0144\7g\2\2\u0144\u0145\7")
        buf.write("c\2\2\u0145\u0146\7m\2\2\u0146\62\3\2\2\2\u0147\u0148")
        buf.write("\7E\2\2\u0148\u0149\7q\2\2\u0149\u014a\7p\2\2\u014a\u014b")
        buf.write("\7v\2\2\u014b\u014c\7k\2\2\u014c\u014d\7p\2\2\u014d\u014e")
        buf.write("\7w\2\2\u014e\u014f\7g\2\2\u014f\64\3\2\2\2\u0150\u0151")
        buf.write("\7K\2\2\u0151\u0152\7h\2\2\u0152\66\3\2\2\2\u0153\u0154")
        buf.write("\7G\2\2\u0154\u0155\7n\2\2\u0155\u0156\7u\2\2\u0156\u0157")
        buf.write("\7g\2\2\u0157\u0158\7k\2\2\u0158\u0159\7h\2\2\u01598\3")
        buf.write("\2\2\2\u015a\u015b\7G\2\2\u015b\u015c\7n\2\2\u015c\u015d")
        buf.write("\7u\2\2\u015d\u015e\7g\2\2\u015e:\3\2\2\2\u015f\u0160")
        buf.write("\7H\2\2\u0160\u0161\7q\2\2\u0161\u0162\7t\2\2\u0162\u0163")
        buf.write("\7g\2\2\u0163\u0164\7c\2\2\u0164\u0165\7e\2\2\u0165\u0166")
        buf.write("\7j\2\2\u0166<\3\2\2\2\u0167\u0168\7V\2\2\u0168\u0169")
        buf.write("\7t\2\2\u0169\u016a\7w\2\2\u016a\u016b\7g\2\2\u016b>\3")
        buf.write("\2\2\2\u016c\u016d\7H\2\2\u016d\u016e\7c\2\2\u016e\u016f")
        buf.write("\7n\2\2\u016f\u0170\7u\2\2\u0170\u0171\7g\2\2\u0171@\3")
        buf.write("\2\2\2\u0172\u0173\7C\2\2\u0173\u0174\7t\2\2\u0174\u0175")
        buf.write("\7t\2\2\u0175\u0176\7c\2\2\u0176\u0177\7{\2\2\u0177B\3")
        buf.write("\2\2\2\u0178\u0179\7K\2\2\u0179\u017a\7p\2\2\u017aD\3")
        buf.write("\2\2\2\u017b\u017c\7K\2\2\u017c\u017d\7p\2\2\u017d\u017e")
        buf.write("\7v\2\2\u017eF\3\2\2\2\u017f\u0180\7H\2\2\u0180\u0181")
        buf.write("\7n\2\2\u0181\u0182\7q\2\2\u0182\u0183\7c\2\2\u0183\u0184")
        buf.write("\7v\2\2\u0184H\3\2\2\2\u0185\u0186\7D\2\2\u0186\u0187")
        buf.write("\7q\2\2\u0187\u0188\7q\2\2\u0188\u0189\7n\2\2\u0189\u018a")
        buf.write("\7g\2\2\u018a\u018b\7c\2\2\u018b\u018c\7p\2\2\u018cJ\3")
        buf.write("\2\2\2\u018d\u018e\7U\2\2\u018e\u018f\7v\2\2\u018f\u0190")
        buf.write("\7t\2\2\u0190\u0191\7k\2\2\u0191\u0192\7p\2\2\u0192\u0193")
        buf.write("\7i\2\2\u0193L\3\2\2\2\u0194\u0195\7T\2\2\u0195\u0196")
        buf.write("\7g\2\2\u0196\u0197\7v\2\2\u0197\u0198\7w\2\2\u0198\u0199")
        buf.write("\7t\2\2\u0199\u019a\7p\2\2\u019aN\3\2\2\2\u019b\u019c")
        buf.write("\7P\2\2\u019c\u019d\7w\2\2\u019d\u019e\7n\2\2\u019e\u019f")
        buf.write("\7n\2\2\u019fP\3\2\2\2\u01a0\u01a1\7E\2\2\u01a1\u01a2")
        buf.write("\7n\2\2\u01a2\u01a3\7c\2\2\u01a3\u01a4\7u\2\2\u01a4\u01a5")
        buf.write("\7u\2\2\u01a5R\3\2\2\2\u01a6\u01a7\7U\2\2\u01a7\u01a8")
        buf.write("\7g\2\2\u01a8\u01a9\7n\2\2\u01a9\u01aa\7h\2\2\u01aaT\3")
        buf.write("\2\2\2\u01ab\u01ac\7X\2\2\u01ac\u01ad\7c\2\2\u01ad\u01ae")
        buf.write("\7n\2\2\u01aeV\3\2\2\2\u01af\u01b0\7X\2\2\u01b0\u01b1")
        buf.write("\7c\2\2\u01b1\u01b2\7t\2\2\u01b2X\3\2\2\2\u01b3\u01b4")
        buf.write("\7E\2\2\u01b4\u01b5\7q\2\2\u01b5\u01b6\7p\2\2\u01b6\u01b7")
        buf.write("\7u\2\2\u01b7\u01b8\7v\2\2\u01b8\u01b9\7t\2\2\u01b9\u01ba")
        buf.write("\7w\2\2\u01ba\u01bb\7e\2\2\u01bb\u01bc\7v\2\2\u01bc\u01bd")
        buf.write("\7q\2\2\u01bd\u01be\7t\2\2\u01beZ\3\2\2\2\u01bf\u01c0")
        buf.write("\7F\2\2\u01c0\u01c1\7g\2\2\u01c1\u01c2\7u\2\2\u01c2\u01c3")
        buf.write("\7v\2\2\u01c3\u01c4\7t\2\2\u01c4\u01c5\7w\2\2\u01c5\u01c6")
        buf.write("\7e\2\2\u01c6\u01c7\7v\2\2\u01c7\u01c8\7q\2\2\u01c8\u01c9")
        buf.write("\7t\2\2\u01c9\\\3\2\2\2\u01ca\u01cb\7P\2\2\u01cb\u01cc")
        buf.write("\7g\2\2\u01cc\u01cd\7y\2\2\u01cd^\3\2\2\2\u01ce\u01cf")
        buf.write("\7D\2\2\u01cf\u01d0\7{\2\2\u01d0`\3\2\2\2\u01d1\u01d2")
        buf.write("\7-\2\2\u01d2b\3\2\2\2\u01d3\u01d4\7/\2\2\u01d4d\3\2\2")
        buf.write("\2\u01d5\u01d6\7,\2\2\u01d6f\3\2\2\2\u01d7\u01d8\7\61")
        buf.write("\2\2\u01d8h\3\2\2\2\u01d9\u01da\7\'\2\2\u01daj\3\2\2\2")
        buf.write("\u01db\u01dc\7#\2\2\u01dcl\3\2\2\2\u01dd\u01de\7(\2\2")
        buf.write("\u01de\u01df\7(\2\2\u01dfn\3\2\2\2\u01e0\u01e1\7~\2\2")
        buf.write("\u01e1\u01e2\7~\2\2\u01e2p\3\2\2\2\u01e3\u01e4\7?\2\2")
        buf.write("\u01e4\u01e5\7?\2\2\u01e5r\3\2\2\2\u01e6\u01e7\7?\2\2")
        buf.write("\u01e7t\3\2\2\2\u01e8\u01e9\7#\2\2\u01e9\u01ea\7?\2\2")
        buf.write("\u01eav\3\2\2\2\u01eb\u01ec\7@\2\2\u01ecx\3\2\2\2\u01ed")
        buf.write("\u01ee\7>\2\2\u01eez\3\2\2\2\u01ef\u01f0\7@\2\2\u01f0")
        buf.write("\u01f1\7?\2\2\u01f1|\3\2\2\2\u01f2\u01f3\7>\2\2\u01f3")
        buf.write("\u01f4\7?\2\2\u01f4~\3\2\2\2\u01f5\u01f6\7?\2\2\u01f6")
        buf.write("\u01f7\7?\2\2\u01f7\u01f8\7\60\2\2\u01f8\u0080\3\2\2\2")
        buf.write("\u01f9\u01fa\7-\2\2\u01fa\u01fb\7\60\2\2\u01fb\u0082\3")
        buf.write("\2\2\2\u01fc\u01fd\7\60\2\2\u01fd\u01fe\7\60\2\2\u01fe")
        buf.write("\u0084\3\2\2\2\u01ff\u0200\7\60\2\2\u0200\u0086\3\2\2")
        buf.write("\2\u0201\u0202\7<\2\2\u0202\u0203\7<\2\2\u0203\u0088\3")
        buf.write("\2\2\2\u0204\u0208\t\21\2\2\u0205\u0207\t\22\2\2\u0206")
        buf.write("\u0205\3\2\2\2\u0207\u020a\3\2\2\2\u0208\u0206\3\2\2\2")
        buf.write("\u0208\u0209\3\2\2\2\u0209\u008a\3\2\2\2\u020a\u0208\3")
        buf.write("\2\2\2\u020b\u020d\7&\2\2\u020c\u020e\t\22\2\2\u020d\u020c")
        buf.write("\3\2\2\2\u020e\u020f\3\2\2\2\u020f\u020d\3\2\2\2\u020f")
        buf.write("\u0210\3\2\2\2\u0210\u008c\3\2\2\2\u0211\u0212\7%\2\2")
        buf.write("\u0212\u0213\7%\2\2\u0213\u0217\3\2\2\2\u0214\u0216\13")
        buf.write("\2\2\2\u0215\u0214\3\2\2\2\u0216\u0219\3\2\2\2\u0217\u0218")
        buf.write("\3\2\2\2\u0217\u0215\3\2\2\2\u0218\u021a\3\2\2\2\u0219")
        buf.write("\u0217\3\2\2\2\u021a\u021b\7%\2\2\u021b\u021c\7%\2\2\u021c")
        buf.write("\u021d\3\2\2\2\u021d\u021e\bG\6\2\u021e\u008e\3\2\2\2")
        buf.write("\u021f\u0221\t\23\2\2\u0220\u021f\3\2\2\2\u0221\u0222")
        buf.write("\3\2\2\2\u0222\u0220\3\2\2\2\u0222\u0223\3\2\2\2\u0223")
        buf.write("\u0224\3\2\2\2\u0224\u0225\bH\6\2\u0225\u0090\3\2\2\2")
        buf.write("\u0226\u022b\t\20\2\2\u0227\u022a\5\33\16\2\u0228\u022a")
        buf.write("\5\31\r\2\u0229\u0227\3\2\2\2\u0229\u0228\3\2\2\2\u022a")
        buf.write("\u022d\3\2\2\2\u022b\u0229\3\2\2\2\u022b\u022c\3\2\2\2")
        buf.write("\u022c\u022f\3\2\2\2\u022d\u022b\3\2\2\2\u022e\u0230\t")
        buf.write("\24\2\2\u022f\u022e\3\2\2\2\u0230\u0231\3\2\2\2\u0231")
        buf.write("\u0232\bI\7\2\u0232\u0092\3\2\2\2\u0233\u0239\t\20\2\2")
        buf.write("\u0234\u0238\5\33\16\2\u0235\u0236\t\r\2\2\u0236\u0238")
        buf.write("\t\20\2\2\u0237\u0234\3\2\2\2\u0237\u0235\3\2\2\2\u0238")
        buf.write("\u023b\3\2\2\2\u0239\u0237\3\2\2\2\u0239\u023a\3\2\2\2")
        buf.write("\u023a\u023e\3\2\2\2\u023b\u0239\3\2\2\2\u023c\u023f\5")
        buf.write("\31\r\2\u023d\u023f\4\n\13\2\u023e\u023c\3\2\2\2\u023e")
        buf.write("\u023d\3\2\2\2\u023f\u0240\3\2\2\2\u0240\u0241\bJ\b\2")
        buf.write("\u0241\u0094\3\2\2\2\u0242\u0243\13\2\2\2\u0243\u0244")
        buf.write("\bK\t\2\u0244\u0096\3\2\2\2$\2\u0099\u009e\u00a5\u00aa")
        buf.write("\u00b0\u00b5\u00bc\u00c1\u00c8\u00d9\u00df\u00e4\u00ea")
        buf.write("\u00ef\u00f6\u00fb\u0101\u0107\u0117\u011c\u0120\u0126")
        buf.write("\u0128\u0208\u020f\u0217\u0222\u0229\u022b\u022f\u0237")
        buf.write("\u0239\u023e\n\3\6\2\3\7\3\3\n\4\3\17\5\b\2\2\3I\6\3J")
        buf.write("\7\3K\b")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    NZINTLIT = 1
    INTLIT = 2
    FLOATLIT = 3
    BOOLIT = 4
    STRINGLIT = 5
    LB = 6
    RB = 7
    LP = 8
    RP = 9
    LSB = 10
    RSB = 11
    COLON = 12
    SEMI = 13
    COMMA = 14
    BREAK = 15
    CONTINUE = 16
    IF = 17
    ELSEIF = 18
    ELSE = 19
    FOREACH = 20
    TRUE = 21
    FALSE = 22
    ARRAY = 23
    IN = 24
    INT = 25
    FLOAT = 26
    BOOLEAN = 27
    STRING = 28
    RETURN = 29
    NULL = 30
    CLASS = 31
    SELF = 32
    VAL = 33
    VAR = 34
    CONSTRUCTOR = 35
    DESTRUCTOR = 36
    NEW = 37
    BY = 38
    ADDOP = 39
    SUBOP = 40
    MULOP = 41
    DIVOP = 42
    MODOP = 43
    NOTOP = 44
    ANDOP = 45
    OROP = 46
    EQLOP = 47
    ASSOP = 48
    IEQOP = 49
    GRTOP = 50
    LSTOP = 51
    GTEOP = 52
    LTEOP = 53
    STRCMP = 54
    CONCAT = 55
    DOTDOT = 56
    DOTOP = 57
    SCOOP = 58
    IDENTIFIERS = 59
    STATIC_MEM = 60
    COMMENT = 61
    WS = 62
    UNCLOSE_STRING = 63
    ILLEGAL_ESCAPE = 64
    ERROR_CHAR = 65

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'{'", "'}'", "'['", "']'", "':'", "';'", "','", 
            "'Break'", "'Continue'", "'If'", "'Elseif'", "'Else'", "'Foreach'", 
            "'True'", "'False'", "'Array'", "'In'", "'Int'", "'Float'", 
            "'Boolean'", "'String'", "'Return'", "'Null'", "'Class'", "'Self'", 
            "'Val'", "'Var'", "'Constructor'", "'Destructor'", "'New'", 
            "'By'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", 
            "'=='", "'='", "'!='", "'>'", "'<'", "'>='", "'<='", "'==.'", 
            "'+.'", "'..'", "'.'", "'::'" ]

    symbolicNames = [ "<INVALID>",
            "NZINTLIT", "INTLIT", "FLOATLIT", "BOOLIT", "STRINGLIT", "LB", 
            "RB", "LP", "RP", "LSB", "RSB", "COLON", "SEMI", "COMMA", "BREAK", 
            "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", "TRUE", "FALSE", 
            "ARRAY", "IN", "INT", "FLOAT", "BOOLEAN", "STRING", "RETURN", 
            "NULL", "CLASS", "SELF", "VAL", "VAR", "CONSTRUCTOR", "DESTRUCTOR", 
            "NEW", "BY", "ADDOP", "SUBOP", "MULOP", "DIVOP", "MODOP", "NOTOP", 
            "ANDOP", "OROP", "EQLOP", "ASSOP", "IEQOP", "GRTOP", "LSTOP", 
            "GTEOP", "LTEOP", "STRCMP", "CONCAT", "DOTDOT", "DOTOP", "SCOOP", 
            "IDENTIFIERS", "STATIC_MEM", "COMMENT", "WS", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "NZDECIMAL", "NZBINARY", "NZOCTAL", "NZHEXA", "NZINTLIT", 
                  "INTLIT", "EXP", "DEC_FLOAT", "FLOATLIT", "BOOLIT", "ESCAPE_SEQUENCES", 
                  "ILLEGAL_ESC_SEQ", "CHARACTER", "STRINGLIT", "LB", "RB", 
                  "LP", "RP", "LSB", "RSB", "COLON", "SEMI", "COMMA", "BREAK", 
                  "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", "TRUE", 
                  "FALSE", "ARRAY", "IN", "INT", "FLOAT", "BOOLEAN", "STRING", 
                  "RETURN", "NULL", "CLASS", "SELF", "VAL", "VAR", "CONSTRUCTOR", 
                  "DESTRUCTOR", "NEW", "BY", "ADDOP", "SUBOP", "MULOP", 
                  "DIVOP", "MODOP", "NOTOP", "ANDOP", "OROP", "EQLOP", "ASSOP", 
                  "IEQOP", "GRTOP", "LSTOP", "GTEOP", "LTEOP", "STRCMP", 
                  "CONCAT", "DOTDOT", "DOTOP", "SCOOP", "IDENTIFIERS", "STATIC_MEM", 
                  "COMMENT", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    grammarFileName = "D96.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[4] = self.NZINTLIT_action 
            actions[5] = self.INTLIT_action 
            actions[8] = self.FLOATLIT_action 
            actions[13] = self.STRINGLIT_action 
            actions[71] = self.UNCLOSE_STRING_action 
            actions[72] = self.ILLEGAL_ESCAPE_action 
            actions[73] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def NZINTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            	self.text = self.text.replace("_", "")

     

    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            	self.text = self.text.replace("_", "")

     

    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            	self.text = self.text.replace("_", "")

     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            	self.text = self.text[1:-1]

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            		y = self.text
            		if y[-1] in ['\r','\n','\f']:
            				raise UncloseString(y[1:-1])
            		else:
            				raise UncloseString(y[1:])
            	
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

            			raise IllegalEscape(self.text[1:]);
            		
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:
            raise ErrorToken(self.text)
     


