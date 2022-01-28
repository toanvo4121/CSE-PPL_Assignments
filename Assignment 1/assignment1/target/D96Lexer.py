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
        buf.write("\3\2\3\2\3\3\3\3\5\3\u009d\n\3\3\3\7\3\u00a0\n\3\f\3\16")
        buf.write("\3\u00a3\13\3\3\4\3\4\3\4\3\4\5\4\u00a9\n\4\3\4\7\4\u00ac")
        buf.write("\n\4\f\4\16\4\u00af\13\4\3\5\3\5\3\5\5\5\u00b4\n\5\3\5")
        buf.write("\7\5\u00b7\n\5\f\5\16\5\u00ba\13\5\3\6\3\6\3\6\3\6\5\6")
        buf.write("\u00c0\n\6\3\6\7\6\u00c3\n\6\f\6\16\6\u00c6\13\6\3\7\3")
        buf.write("\7\3\7\3\7\5\7\u00cc\n\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u00dd\n\b\3\b\3\b\3")
        buf.write("\t\3\t\5\t\u00e3\n\t\3\t\6\t\u00e6\n\t\r\t\16\t\u00e7")
        buf.write("\3\n\3\n\7\n\u00ec\n\n\f\n\16\n\u00ef\13\n\3\13\3\13\5")
        buf.write("\13\u00f3\n\13\3\13\3\13\3\13\3\13\3\13\5\13\u00fa\n\13")
        buf.write("\3\13\3\13\3\13\5\13\u00ff\n\13\3\13\3\13\3\13\3\13\5")
        buf.write("\13\u0105\n\13\3\13\3\13\3\f\3\f\5\f\u010b\n\f\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u011b")
        buf.write("\n\r\3\16\3\16\3\16\5\16\u0120\n\16\3\17\3\17\5\17\u0124")
        buf.write("\n\17\3\20\3\20\3\20\3\20\7\20\u012a\n\20\f\20\16\20\u012d")
        buf.write("\13\20\3\20\3\20\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3")
        buf.write("\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30")
        buf.write("\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3!")
        buf.write("\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3$\3")
        buf.write("$\3$\3$\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3&\3&\3\'")
        buf.write("\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3(\3)\3)\3")
        buf.write(")\3)\3)\3*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3,\3,\3,\3,\3")
        buf.write("-\3-\3-\3-\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3/\3/\3")
        buf.write("/\3/\3/\3/\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3\61\3\61")
        buf.write("\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66")
        buf.write("\3\67\3\67\38\38\38\39\39\39\3:\3:\3:\3;\3;\3<\3<\3<\3")
        buf.write("=\3=\3>\3>\3?\3?\3?\3@\3@\3@\3A\3A\3A\3A\3B\3B\3B\3C\3")
        buf.write("C\3D\3D\3D\3E\3E\7E\u0207\nE\fE\16E\u020a\13E\3F\3F\6")
        buf.write("F\u020e\nF\rF\16F\u020f\3G\3G\3G\3G\7G\u0216\nG\fG\16")
        buf.write("G\u0219\13G\3G\3G\3G\3G\3G\3H\6H\u0221\nH\rH\16H\u0222")
        buf.write("\3H\3H\3I\3I\3I\3I\3I\7I\u022c\nI\fI\16I\u022f\13I\3I")
        buf.write("\5I\u0232\nI\3I\3I\3J\3J\3J\3J\7J\u023a\nJ\fJ\16J\u023d")
        buf.write("\13J\3J\3J\3J\3J\3K\3K\3K\3\u0217\2L\3\3\5\2\7\2\t\2\13")
        buf.write("\2\r\4\17\5\21\2\23\2\25\6\27\7\31\2\33\2\35\2\37\b!\t")
        buf.write("#\n%\13\'\f)\r+\16-\17/\20\61\21\63\22\65\23\67\249\25")
        buf.write(";\26=\27?\30A\31C\32E\33G\34I\35K\36M\37O Q!S\"U#W$Y%")
        buf.write("[&]\'_(a)c*e+g,i-k.m/o\60q\61s\62u\63w\64y\65{\66}\67")
        buf.write("\1778\u00819\u0083:\u0085;\u0087<\u0089=\u008b>\u008d")
        buf.write("?\u008f@\u0091A\u0093B\u0095C\3\2\25\3\2\63;\3\2\62;\4")
        buf.write("\2DDdd\3\2\62\63\3\2\639\3\2\629\4\2ZZzz\4\2\63;CH\4\2")
        buf.write("\62;CH\4\2GGgg\4\2--//\3\2))\n\2$$))^^ddhhppttvv\6\2\f")
        buf.write("\f\16\17$$^^\3\2$$\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f")
        buf.write("\17\17\"\"\4\3\f\f\16\17\2\u026a\2\3\3\2\2\2\2\r\3\2\2")
        buf.write("\2\2\17\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\37\3\2\2\2")
        buf.write("\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2")
        buf.write("\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2")
        buf.write("\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2")
        buf.write("\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3")
        buf.write("\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y")
        buf.write("\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2")
        buf.write("c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2")
        buf.write("\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2")
        buf.write("\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3")
        buf.write("\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2")
        buf.write("\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d")
        buf.write("\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2")
        buf.write("\2\2\u0095\3\2\2\2\3\u0097\3\2\2\2\5\u009a\3\2\2\2\7\u00a4")
        buf.write("\3\2\2\2\t\u00b0\3\2\2\2\13\u00bb\3\2\2\2\r\u00cb\3\2")
        buf.write("\2\2\17\u00dc\3\2\2\2\21\u00e0\3\2\2\2\23\u00e9\3\2\2")
        buf.write("\2\25\u0104\3\2\2\2\27\u010a\3\2\2\2\31\u011a\3\2\2\2")
        buf.write("\33\u011f\3\2\2\2\35\u0123\3\2\2\2\37\u0125\3\2\2\2!\u0132")
        buf.write("\3\2\2\2#\u0134\3\2\2\2%\u0136\3\2\2\2\'\u0138\3\2\2\2")
        buf.write(")\u013a\3\2\2\2+\u013c\3\2\2\2-\u013e\3\2\2\2/\u0140\3")
        buf.write("\2\2\2\61\u0142\3\2\2\2\63\u0144\3\2\2\2\65\u014a\3\2")
        buf.write("\2\2\67\u0153\3\2\2\29\u0156\3\2\2\2;\u015d\3\2\2\2=\u0162")
        buf.write("\3\2\2\2?\u016a\3\2\2\2A\u016f\3\2\2\2C\u0175\3\2\2\2")
        buf.write("E\u017b\3\2\2\2G\u017e\3\2\2\2I\u0182\3\2\2\2K\u0188\3")
        buf.write("\2\2\2M\u0190\3\2\2\2O\u0197\3\2\2\2Q\u019e\3\2\2\2S\u01a3")
        buf.write("\3\2\2\2U\u01a9\3\2\2\2W\u01ae\3\2\2\2Y\u01b2\3\2\2\2")
        buf.write("[\u01b6\3\2\2\2]\u01c2\3\2\2\2_\u01cd\3\2\2\2a\u01d1\3")
        buf.write("\2\2\2c\u01d4\3\2\2\2e\u01d6\3\2\2\2g\u01d8\3\2\2\2i\u01da")
        buf.write("\3\2\2\2k\u01dc\3\2\2\2m\u01de\3\2\2\2o\u01e0\3\2\2\2")
        buf.write("q\u01e3\3\2\2\2s\u01e6\3\2\2\2u\u01e9\3\2\2\2w\u01eb\3")
        buf.write("\2\2\2y\u01ee\3\2\2\2{\u01f0\3\2\2\2}\u01f2\3\2\2\2\177")
        buf.write("\u01f5\3\2\2\2\u0081\u01f8\3\2\2\2\u0083\u01fc\3\2\2\2")
        buf.write("\u0085\u01ff\3\2\2\2\u0087\u0201\3\2\2\2\u0089\u0204\3")
        buf.write("\2\2\2\u008b\u020b\3\2\2\2\u008d\u0211\3\2\2\2\u008f\u0220")
        buf.write("\3\2\2\2\u0091\u0226\3\2\2\2\u0093\u0235\3\2\2\2\u0095")
        buf.write("\u0242\3\2\2\2\u0097\u0098\7\60\2\2\u0098\u0099\7\60\2")
        buf.write("\2\u0099\4\3\2\2\2\u009a\u00a1\t\2\2\2\u009b\u009d\7a")
        buf.write("\2\2\u009c\u009b\3\2\2\2\u009c\u009d\3\2\2\2\u009d\u009e")
        buf.write("\3\2\2\2\u009e\u00a0\t\3\2\2\u009f\u009c\3\2\2\2\u00a0")
        buf.write("\u00a3\3\2\2\2\u00a1\u009f\3\2\2\2\u00a1\u00a2\3\2\2\2")
        buf.write("\u00a2\6\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a4\u00a5\7\62")
        buf.write("\2\2\u00a5\u00a6\t\4\2\2\u00a6\u00ad\7\63\2\2\u00a7\u00a9")
        buf.write("\7a\2\2\u00a8\u00a7\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9")
        buf.write("\u00aa\3\2\2\2\u00aa\u00ac\t\5\2\2\u00ab\u00a8\3\2\2\2")
        buf.write("\u00ac\u00af\3\2\2\2\u00ad\u00ab\3\2\2\2\u00ad\u00ae\3")
        buf.write("\2\2\2\u00ae\b\3\2\2\2\u00af\u00ad\3\2\2\2\u00b0\u00b1")
        buf.write("\7\62\2\2\u00b1\u00b8\t\6\2\2\u00b2\u00b4\7a\2\2\u00b3")
        buf.write("\u00b2\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4\u00b5\3\2\2\2")
        buf.write("\u00b5\u00b7\t\7\2\2\u00b6\u00b3\3\2\2\2\u00b7\u00ba\3")
        buf.write("\2\2\2\u00b8\u00b6\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b9\n")
        buf.write("\3\2\2\2\u00ba\u00b8\3\2\2\2\u00bb\u00bc\7\62\2\2\u00bc")
        buf.write("\u00bd\t\b\2\2\u00bd\u00c4\t\t\2\2\u00be\u00c0\7a\2\2")
        buf.write("\u00bf\u00be\3\2\2\2\u00bf\u00c0\3\2\2\2\u00c0\u00c1\3")
        buf.write("\2\2\2\u00c1\u00c3\t\n\2\2\u00c2\u00bf\3\2\2\2\u00c3\u00c6")
        buf.write("\3\2\2\2\u00c4\u00c2\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5")
        buf.write("\f\3\2\2\2\u00c6\u00c4\3\2\2\2\u00c7\u00cc\5\5\3\2\u00c8")
        buf.write("\u00cc\5\7\4\2\u00c9\u00cc\5\t\5\2\u00ca\u00cc\5\13\6")
        buf.write("\2\u00cb\u00c7\3\2\2\2\u00cb\u00c8\3\2\2\2\u00cb\u00c9")
        buf.write("\3\2\2\2\u00cb\u00ca\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cd")
        buf.write("\u00ce\b\7\2\2\u00ce\16\3\2\2\2\u00cf\u00dd\5\5\3\2\u00d0")
        buf.write("\u00dd\5\7\4\2\u00d1\u00dd\5\t\5\2\u00d2\u00dd\5\13\6")
        buf.write("\2\u00d3\u00dd\7\62\2\2\u00d4\u00d5\7\62\2\2\u00d5\u00d6")
        buf.write("\t\b\2\2\u00d6\u00dd\7\62\2\2\u00d7\u00d8\7\62\2\2\u00d8")
        buf.write("\u00d9\t\4\2\2\u00d9\u00dd\7\62\2\2\u00da\u00db\7\62\2")
        buf.write("\2\u00db\u00dd\7\62\2\2\u00dc\u00cf\3\2\2\2\u00dc\u00d0")
        buf.write("\3\2\2\2\u00dc\u00d1\3\2\2\2\u00dc\u00d2\3\2\2\2\u00dc")
        buf.write("\u00d3\3\2\2\2\u00dc\u00d4\3\2\2\2\u00dc\u00d7\3\2\2\2")
        buf.write("\u00dc\u00da\3\2\2\2\u00dd\u00de\3\2\2\2\u00de\u00df\b")
        buf.write("\b\3\2\u00df\20\3\2\2\2\u00e0\u00e2\t\13\2\2\u00e1\u00e3")
        buf.write("\t\f\2\2\u00e2\u00e1\3\2\2\2\u00e2\u00e3\3\2\2\2\u00e3")
        buf.write("\u00e5\3\2\2\2\u00e4\u00e6\t\3\2\2\u00e5\u00e4\3\2\2\2")
        buf.write("\u00e6\u00e7\3\2\2\2\u00e7\u00e5\3\2\2\2\u00e7\u00e8\3")
        buf.write("\2\2\2\u00e8\22\3\2\2\2\u00e9\u00ed\7\60\2\2\u00ea\u00ec")
        buf.write("\t\3\2\2\u00eb\u00ea\3\2\2\2\u00ec\u00ef\3\2\2\2\u00ed")
        buf.write("\u00eb\3\2\2\2\u00ed\u00ee\3\2\2\2\u00ee\24\3\2\2\2\u00ef")
        buf.write("\u00ed\3\2\2\2\u00f0\u00f3\5\5\3\2\u00f1\u00f3\7\62\2")
        buf.write("\2\u00f2\u00f0\3\2\2\2\u00f2\u00f1\3\2\2\2\u00f3\u00f4")
        buf.write("\3\2\2\2\u00f4\u00f5\5\23\n\2\u00f5\u00f6\5\21\t\2\u00f6")
        buf.write("\u0105\3\2\2\2\u00f7\u00fa\5\5\3\2\u00f8\u00fa\7\62\2")
        buf.write("\2\u00f9\u00f7\3\2\2\2\u00f9\u00f8\3\2\2\2\u00fa\u00fb")
        buf.write("\3\2\2\2\u00fb\u0105\5\23\n\2\u00fc\u00ff\5\5\3\2\u00fd")
        buf.write("\u00ff\7\62\2\2\u00fe\u00fc\3\2\2\2\u00fe\u00fd\3\2\2")
        buf.write("\2\u00ff\u0100\3\2\2\2\u0100\u0105\5\21\t\2\u0101\u0102")
        buf.write("\5\23\n\2\u0102\u0103\5\21\t\2\u0103\u0105\3\2\2\2\u0104")
        buf.write("\u00f2\3\2\2\2\u0104\u00f9\3\2\2\2\u0104\u00fe\3\2\2\2")
        buf.write("\u0104\u0101\3\2\2\2\u0105\u0106\3\2\2\2\u0106\u0107\b")
        buf.write("\13\4\2\u0107\26\3\2\2\2\u0108\u010b\5? \2\u0109\u010b")
        buf.write("\5A!\2\u010a\u0108\3\2\2\2\u010a\u0109\3\2\2\2\u010b\30")
        buf.write("\3\2\2\2\u010c\u010d\7^\2\2\u010d\u011b\7d\2\2\u010e\u010f")
        buf.write("\7^\2\2\u010f\u011b\7h\2\2\u0110\u0111\7^\2\2\u0111\u011b")
        buf.write("\7p\2\2\u0112\u0113\7^\2\2\u0113\u011b\7t\2\2\u0114\u0115")
        buf.write("\7^\2\2\u0115\u011b\7v\2\2\u0116\u0117\7^\2\2\u0117\u011b")
        buf.write("\7^\2\2\u0118\u0119\7^\2\2\u0119\u011b\t\r\2\2\u011a\u010c")
        buf.write("\3\2\2\2\u011a\u010e\3\2\2\2\u011a\u0110\3\2\2\2\u011a")
        buf.write("\u0112\3\2\2\2\u011a\u0114\3\2\2\2\u011a\u0116\3\2\2\2")
        buf.write("\u011a\u0118\3\2\2\2\u011b\32\3\2\2\2\u011c\u011d\7^\2")
        buf.write("\2\u011d\u0120\n\16\2\2\u011e\u0120\7^\2\2\u011f\u011c")
        buf.write("\3\2\2\2\u011f\u011e\3\2\2\2\u0120\34\3\2\2\2\u0121\u0124")
        buf.write("\n\17\2\2\u0122\u0124\5\31\r\2\u0123\u0121\3\2\2\2\u0123")
        buf.write("\u0122\3\2\2\2\u0124\36\3\2\2\2\u0125\u012b\t\20\2\2\u0126")
        buf.write("\u012a\5\35\17\2\u0127\u0128\t\r\2\2\u0128\u012a\t\20")
        buf.write("\2\2\u0129\u0126\3\2\2\2\u0129\u0127\3\2\2\2\u012a\u012d")
        buf.write("\3\2\2\2\u012b\u0129\3\2\2\2\u012b\u012c\3\2\2\2\u012c")
        buf.write("\u012e\3\2\2\2\u012d\u012b\3\2\2\2\u012e\u012f\t\20\2")
        buf.write("\2\u012f\u0130\3\2\2\2\u0130\u0131\b\20\5\2\u0131 \3\2")
        buf.write("\2\2\u0132\u0133\7*\2\2\u0133\"\3\2\2\2\u0134\u0135\7")
        buf.write("+\2\2\u0135$\3\2\2\2\u0136\u0137\7}\2\2\u0137&\3\2\2\2")
        buf.write("\u0138\u0139\7\177\2\2\u0139(\3\2\2\2\u013a\u013b\7]\2")
        buf.write("\2\u013b*\3\2\2\2\u013c\u013d\7_\2\2\u013d,\3\2\2\2\u013e")
        buf.write("\u013f\7<\2\2\u013f.\3\2\2\2\u0140\u0141\7=\2\2\u0141")
        buf.write("\60\3\2\2\2\u0142\u0143\7.\2\2\u0143\62\3\2\2\2\u0144")
        buf.write("\u0145\7D\2\2\u0145\u0146\7t\2\2\u0146\u0147\7g\2\2\u0147")
        buf.write("\u0148\7c\2\2\u0148\u0149\7m\2\2\u0149\64\3\2\2\2\u014a")
        buf.write("\u014b\7E\2\2\u014b\u014c\7q\2\2\u014c\u014d\7p\2\2\u014d")
        buf.write("\u014e\7v\2\2\u014e\u014f\7k\2\2\u014f\u0150\7p\2\2\u0150")
        buf.write("\u0151\7w\2\2\u0151\u0152\7g\2\2\u0152\66\3\2\2\2\u0153")
        buf.write("\u0154\7K\2\2\u0154\u0155\7h\2\2\u01558\3\2\2\2\u0156")
        buf.write("\u0157\7G\2\2\u0157\u0158\7n\2\2\u0158\u0159\7u\2\2\u0159")
        buf.write("\u015a\7g\2\2\u015a\u015b\7k\2\2\u015b\u015c\7h\2\2\u015c")
        buf.write(":\3\2\2\2\u015d\u015e\7G\2\2\u015e\u015f\7n\2\2\u015f")
        buf.write("\u0160\7u\2\2\u0160\u0161\7g\2\2\u0161<\3\2\2\2\u0162")
        buf.write("\u0163\7H\2\2\u0163\u0164\7q\2\2\u0164\u0165\7t\2\2\u0165")
        buf.write("\u0166\7g\2\2\u0166\u0167\7c\2\2\u0167\u0168\7e\2\2\u0168")
        buf.write("\u0169\7j\2\2\u0169>\3\2\2\2\u016a\u016b\7V\2\2\u016b")
        buf.write("\u016c\7t\2\2\u016c\u016d\7w\2\2\u016d\u016e\7g\2\2\u016e")
        buf.write("@\3\2\2\2\u016f\u0170\7H\2\2\u0170\u0171\7c\2\2\u0171")
        buf.write("\u0172\7n\2\2\u0172\u0173\7u\2\2\u0173\u0174\7g\2\2\u0174")
        buf.write("B\3\2\2\2\u0175\u0176\7C\2\2\u0176\u0177\7t\2\2\u0177")
        buf.write("\u0178\7t\2\2\u0178\u0179\7c\2\2\u0179\u017a\7{\2\2\u017a")
        buf.write("D\3\2\2\2\u017b\u017c\7K\2\2\u017c\u017d\7p\2\2\u017d")
        buf.write("F\3\2\2\2\u017e\u017f\7K\2\2\u017f\u0180\7p\2\2\u0180")
        buf.write("\u0181\7v\2\2\u0181H\3\2\2\2\u0182\u0183\7H\2\2\u0183")
        buf.write("\u0184\7n\2\2\u0184\u0185\7q\2\2\u0185\u0186\7c\2\2\u0186")
        buf.write("\u0187\7v\2\2\u0187J\3\2\2\2\u0188\u0189\7D\2\2\u0189")
        buf.write("\u018a\7q\2\2\u018a\u018b\7q\2\2\u018b\u018c\7n\2\2\u018c")
        buf.write("\u018d\7g\2\2\u018d\u018e\7c\2\2\u018e\u018f\7p\2\2\u018f")
        buf.write("L\3\2\2\2\u0190\u0191\7U\2\2\u0191\u0192\7v\2\2\u0192")
        buf.write("\u0193\7t\2\2\u0193\u0194\7k\2\2\u0194\u0195\7p\2\2\u0195")
        buf.write("\u0196\7i\2\2\u0196N\3\2\2\2\u0197\u0198\7T\2\2\u0198")
        buf.write("\u0199\7g\2\2\u0199\u019a\7v\2\2\u019a\u019b\7w\2\2\u019b")
        buf.write("\u019c\7t\2\2\u019c\u019d\7p\2\2\u019dP\3\2\2\2\u019e")
        buf.write("\u019f\7P\2\2\u019f\u01a0\7w\2\2\u01a0\u01a1\7n\2\2\u01a1")
        buf.write("\u01a2\7n\2\2\u01a2R\3\2\2\2\u01a3\u01a4\7E\2\2\u01a4")
        buf.write("\u01a5\7n\2\2\u01a5\u01a6\7c\2\2\u01a6\u01a7\7u\2\2\u01a7")
        buf.write("\u01a8\7u\2\2\u01a8T\3\2\2\2\u01a9\u01aa\7U\2\2\u01aa")
        buf.write("\u01ab\7g\2\2\u01ab\u01ac\7n\2\2\u01ac\u01ad\7h\2\2\u01ad")
        buf.write("V\3\2\2\2\u01ae\u01af\7X\2\2\u01af\u01b0\7c\2\2\u01b0")
        buf.write("\u01b1\7n\2\2\u01b1X\3\2\2\2\u01b2\u01b3\7X\2\2\u01b3")
        buf.write("\u01b4\7c\2\2\u01b4\u01b5\7t\2\2\u01b5Z\3\2\2\2\u01b6")
        buf.write("\u01b7\7E\2\2\u01b7\u01b8\7q\2\2\u01b8\u01b9\7p\2\2\u01b9")
        buf.write("\u01ba\7u\2\2\u01ba\u01bb\7v\2\2\u01bb\u01bc\7t\2\2\u01bc")
        buf.write("\u01bd\7w\2\2\u01bd\u01be\7e\2\2\u01be\u01bf\7v\2\2\u01bf")
        buf.write("\u01c0\7q\2\2\u01c0\u01c1\7t\2\2\u01c1\\\3\2\2\2\u01c2")
        buf.write("\u01c3\7F\2\2\u01c3\u01c4\7g\2\2\u01c4\u01c5\7u\2\2\u01c5")
        buf.write("\u01c6\7v\2\2\u01c6\u01c7\7t\2\2\u01c7\u01c8\7w\2\2\u01c8")
        buf.write("\u01c9\7e\2\2\u01c9\u01ca\7v\2\2\u01ca\u01cb\7q\2\2\u01cb")
        buf.write("\u01cc\7t\2\2\u01cc^\3\2\2\2\u01cd\u01ce\7P\2\2\u01ce")
        buf.write("\u01cf\7g\2\2\u01cf\u01d0\7y\2\2\u01d0`\3\2\2\2\u01d1")
        buf.write("\u01d2\7D\2\2\u01d2\u01d3\7{\2\2\u01d3b\3\2\2\2\u01d4")
        buf.write("\u01d5\7-\2\2\u01d5d\3\2\2\2\u01d6\u01d7\7/\2\2\u01d7")
        buf.write("f\3\2\2\2\u01d8\u01d9\7,\2\2\u01d9h\3\2\2\2\u01da\u01db")
        buf.write("\7\61\2\2\u01dbj\3\2\2\2\u01dc\u01dd\7\'\2\2\u01ddl\3")
        buf.write("\2\2\2\u01de\u01df\7#\2\2\u01dfn\3\2\2\2\u01e0\u01e1\7")
        buf.write("(\2\2\u01e1\u01e2\7(\2\2\u01e2p\3\2\2\2\u01e3\u01e4\7")
        buf.write("~\2\2\u01e4\u01e5\7~\2\2\u01e5r\3\2\2\2\u01e6\u01e7\7")
        buf.write("?\2\2\u01e7\u01e8\7?\2\2\u01e8t\3\2\2\2\u01e9\u01ea\7")
        buf.write("?\2\2\u01eav\3\2\2\2\u01eb\u01ec\7#\2\2\u01ec\u01ed\7")
        buf.write("?\2\2\u01edx\3\2\2\2\u01ee\u01ef\7@\2\2\u01efz\3\2\2\2")
        buf.write("\u01f0\u01f1\7>\2\2\u01f1|\3\2\2\2\u01f2\u01f3\7@\2\2")
        buf.write("\u01f3\u01f4\7?\2\2\u01f4~\3\2\2\2\u01f5\u01f6\7>\2\2")
        buf.write("\u01f6\u01f7\7?\2\2\u01f7\u0080\3\2\2\2\u01f8\u01f9\7")
        buf.write("?\2\2\u01f9\u01fa\7?\2\2\u01fa\u01fb\7\60\2\2\u01fb\u0082")
        buf.write("\3\2\2\2\u01fc\u01fd\7-\2\2\u01fd\u01fe\7\60\2\2\u01fe")
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
        buf.write("\u0226\u022d\t\20\2\2\u0227\u022c\5\35\17\2\u0228\u022c")
        buf.write("\5\33\16\2\u0229\u022a\t\r\2\2\u022a\u022c\t\20\2\2\u022b")
        buf.write("\u0227\3\2\2\2\u022b\u0228\3\2\2\2\u022b\u0229\3\2\2\2")
        buf.write("\u022c\u022f\3\2\2\2\u022d\u022b\3\2\2\2\u022d\u022e\3")
        buf.write("\2\2\2\u022e\u0231\3\2\2\2\u022f\u022d\3\2\2\2\u0230\u0232")
        buf.write("\t\24\2\2\u0231\u0230\3\2\2\2\u0232\u0233\3\2\2\2\u0233")
        buf.write("\u0234\bI\7\2\u0234\u0092\3\2\2\2\u0235\u023b\t\20\2\2")
        buf.write("\u0236\u023a\5\35\17\2\u0237\u0238\t\r\2\2\u0238\u023a")
        buf.write("\t\20\2\2\u0239\u0236\3\2\2\2\u0239\u0237\3\2\2\2\u023a")
        buf.write("\u023d\3\2\2\2\u023b\u0239\3\2\2\2\u023b\u023c\3\2\2\2")
        buf.write("\u023c\u023e\3\2\2\2\u023d\u023b\3\2\2\2\u023e\u023f\5")
        buf.write("\33\16\2\u023f\u0240\3\2\2\2\u0240\u0241\bJ\b\2\u0241")
        buf.write("\u0094\3\2\2\2\u0242\u0243\13\2\2\2\u0243\u0244\bK\t\2")
        buf.write("\u0244\u0096\3\2\2\2#\2\u009c\u00a1\u00a8\u00ad\u00b3")
        buf.write("\u00b8\u00bf\u00c4\u00cb\u00dc\u00e2\u00e7\u00ed\u00f2")
        buf.write("\u00f9\u00fe\u0104\u010a\u011a\u011f\u0123\u0129\u012b")
        buf.write("\u0208\u020f\u0217\u0222\u022b\u022d\u0231\u0239\u023b")
        buf.write("\n\3\7\2\3\b\3\3\13\4\3\20\5\b\2\2\3I\6\3J\7\3K\b")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    NZINTLIT = 2
    INTLIT = 3
    FLOATLIT = 4
    BOOLIT = 5
    STRINGLIT = 6
    LB = 7
    RB = 8
    LP = 9
    RP = 10
    LSB = 11
    RSB = 12
    COLON = 13
    SEMI = 14
    COMMA = 15
    BREAK = 16
    CONTINUE = 17
    IF = 18
    ELSEIF = 19
    ELSE = 20
    FOREACH = 21
    TRUE = 22
    FALSE = 23
    ARRAY = 24
    IN = 25
    INT = 26
    FLOAT = 27
    BOOLEAN = 28
    STRING = 29
    RETURN = 30
    NULL = 31
    CLASS = 32
    SELF = 33
    VAL = 34
    VAR = 35
    CONSTRUCTOR = 36
    DESTRUCTOR = 37
    NEW = 38
    BY = 39
    ADDOP = 40
    SUBOP = 41
    MULOP = 42
    DIVOP = 43
    MODOP = 44
    NOTOP = 45
    ANDOP = 46
    OROP = 47
    EQLOP = 48
    ASSOP = 49
    IEQOP = 50
    GRTOP = 51
    LSTOP = 52
    GTEOP = 53
    LTEOP = 54
    STRCMP = 55
    CONCAT = 56
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
            "'..'", "'('", "')'", "'{'", "'}'", "'['", "']'", "':'", "';'", 
            "','", "'Break'", "'Continue'", "'If'", "'Elseif'", "'Else'", 
            "'Foreach'", "'True'", "'False'", "'Array'", "'In'", "'Int'", 
            "'Float'", "'Boolean'", "'String'", "'Return'", "'Null'", "'Class'", 
            "'Self'", "'Val'", "'Var'", "'Constructor'", "'Destructor'", 
            "'New'", "'By'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", 
            "'||'", "'=='", "'='", "'!='", "'>'", "'<'", "'>='", "'<='", 
            "'==.'", "'+.'", "'.'", "'::'" ]

    symbolicNames = [ "<INVALID>",
            "NZINTLIT", "INTLIT", "FLOATLIT", "BOOLIT", "STRINGLIT", "LB", 
            "RB", "LP", "RP", "LSB", "RSB", "COLON", "SEMI", "COMMA", "BREAK", 
            "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", "TRUE", "FALSE", 
            "ARRAY", "IN", "INT", "FLOAT", "BOOLEAN", "STRING", "RETURN", 
            "NULL", "CLASS", "SELF", "VAL", "VAR", "CONSTRUCTOR", "DESTRUCTOR", 
            "NEW", "BY", "ADDOP", "SUBOP", "MULOP", "DIVOP", "MODOP", "NOTOP", 
            "ANDOP", "OROP", "EQLOP", "ASSOP", "IEQOP", "GRTOP", "LSTOP", 
            "GTEOP", "LTEOP", "STRCMP", "CONCAT", "DOTOP", "SCOOP", "IDENTIFIERS", 
            "STATIC_MEM", "COMMENT", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "ERROR_CHAR" ]

    ruleNames = [ "T__0", "NZDECIMAL", "NZBINARY", "NZOCTAL", "NZHEXA", 
                  "NZINTLIT", "INTLIT", "EXP", "DEC_FLOAT", "FLOATLIT", 
                  "BOOLIT", "ESCAPE_SEQUENCES", "ILLEGAL_ESC_SEQ", "CHARACTER", 
                  "STRINGLIT", "LB", "RB", "LP", "RP", "LSB", "RSB", "COLON", 
                  "SEMI", "COMMA", "BREAK", "CONTINUE", "IF", "ELSEIF", 
                  "ELSE", "FOREACH", "TRUE", "FALSE", "ARRAY", "IN", "INT", 
                  "FLOAT", "BOOLEAN", "STRING", "RETURN", "NULL", "CLASS", 
                  "SELF", "VAL", "VAR", "CONSTRUCTOR", "DESTRUCTOR", "NEW", 
                  "BY", "ADDOP", "SUBOP", "MULOP", "DIVOP", "MODOP", "NOTOP", 
                  "ANDOP", "OROP", "EQLOP", "ASSOP", "IEQOP", "GRTOP", "LSTOP", 
                  "GTEOP", "LTEOP", "STRCMP", "CONCAT", "DOTOP", "SCOOP", 
                  "IDENTIFIERS", "STATIC_MEM", "COMMENT", "WS", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

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
            actions[5] = self.NZINTLIT_action 
            actions[6] = self.INTLIT_action 
            actions[9] = self.FLOATLIT_action 
            actions[14] = self.STRINGLIT_action 
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
     


