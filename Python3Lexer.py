# Generated from Python3.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from Python3Parser import Python3Parser
from antlr4.Token import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2C")
        buf.write("\u01b7\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\3\2\3\2\3\3\3\3")
        buf.write("\3\3\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3\7\3")
        buf.write("\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13\3\f")
        buf.write("\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\17")
        buf.write("\3\17\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31")
        buf.write("\3\32\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"")
        buf.write("\3#\3#\3#\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3%\3%\3")
        buf.write("%\3%\3%\5%\u0124\n%\3%\5%\u0127\n%\5%\u0129\n%\3%\3%\3")
        buf.write("&\3&\7&\u012f\n&\f&\16&\u0132\13&\3\'\5\'\u0135\n\'\3")
        buf.write("\'\3\'\3(\3(\7(\u013b\n(\f(\16(\u013e\13(\3(\5(\u0141")
        buf.write("\n(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60")
        buf.write("\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66")
        buf.write("\3\66\3\67\3\67\3\67\38\38\38\39\39\39\3:\3:\3:\3;\3;")
        buf.write("\3<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3@\3A\3A\3A\6A\u017b\n")
        buf.write("A\rA\16A\u017c\3A\3A\3B\3B\3C\5C\u0184\nC\3D\3D\5D\u0188")
        buf.write("\nD\3E\3E\3E\7E\u018d\nE\fE\16E\u0190\13E\3E\3E\3E\3E")
        buf.write("\7E\u0196\nE\fE\16E\u0199\13E\3E\5E\u019c\nE\3F\3F\3F")
        buf.write("\3G\6G\u01a2\nG\rG\16G\u01a3\3H\3H\7H\u01a8\nH\fH\16H")
        buf.write("\u01ab\13H\3I\3I\5I\u01af\nI\3I\5I\u01b2\nI\3I\3I\5I\u01b6")
        buf.write("\nI\2\2J\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f")
        buf.write("\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27")
        buf.write("-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%")
        buf.write("I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67")
        buf.write("m8o9q:s;u<w=y>{?}@\177A\u0081B\u0083C\u0085\2\u0087\2")
        buf.write("\u0089\2\u008b\2\u008d\2\u008f\2\u0091\2\3\2\n\4\2\f\f")
        buf.write("\16\17\4\2TTtt\3\2\63;\3\2\62;\3\2\62\62\5\2C\\aac|\6")
        buf.write("\2\f\f\16\17))^^\4\2\13\13\"\"\2\u01c4\2\3\3\2\2\2\2\5")
        buf.write("\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2")
        buf.write("\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2")
        buf.write("\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2")
        buf.write("\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2")
        buf.write("\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3")
        buf.write("\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M")
        buf.write("\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2")
        buf.write("W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2")
        buf.write("\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2")
        buf.write("\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2")
        buf.write("\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3")
        buf.write("\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\3")
        buf.write("\u0093\3\2\2\2\5\u0095\3\2\2\2\7\u0098\3\2\2\2\t\u009b")
        buf.write("\3\2\2\2\13\u009e\3\2\2\2\r\u00a1\3\2\2\2\17\u00a4\3\2")
        buf.write("\2\2\21\u00a7\3\2\2\2\23\u00aa\3\2\2\2\25\u00ad\3\2\2")
        buf.write("\2\27\u00b0\3\2\2\2\31\u00b4\3\2\2\2\33\u00b8\3\2\2\2")
        buf.write("\35\u00bc\3\2\2\2\37\u00c0\3\2\2\2!\u00c3\3\2\2\2#\u00c5")
        buf.write("\3\2\2\2%\u00c7\3\2\2\2\'\u00cb\3\2\2\2)\u00d2\3\2\2\2")
        buf.write("+\u00d5\3\2\2\2-\u00da\3\2\2\2/\u00df\3\2\2\2\61\u00e5")
        buf.write("\3\2\2\2\63\u00e9\3\2\2\2\65\u00ec\3\2\2\2\67\u00ef\3")
        buf.write("\2\2\29\u00f3\3\2\2\2;\u00f7\3\2\2\2=\u00fa\3\2\2\2?\u00ff")
        buf.write("\3\2\2\2A\u0104\3\2\2\2C\u010a\3\2\2\2E\u010f\3\2\2\2")
        buf.write("G\u0118\3\2\2\2I\u0128\3\2\2\2K\u012c\3\2\2\2M\u0134\3")
        buf.write("\2\2\2O\u0140\3\2\2\2Q\u0142\3\2\2\2S\u0144\3\2\2\2U\u0146")
        buf.write("\3\2\2\2W\u0148\3\2\2\2Y\u014a\3\2\2\2[\u014c\3\2\2\2")
        buf.write("]\u014e\3\2\2\2_\u0150\3\2\2\2a\u0152\3\2\2\2c\u0154\3")
        buf.write("\2\2\2e\u0156\3\2\2\2g\u0158\3\2\2\2i\u015a\3\2\2\2k\u015c")
        buf.write("\3\2\2\2m\u015e\3\2\2\2o\u0161\3\2\2\2q\u0164\3\2\2\2")
        buf.write("s\u0167\3\2\2\2u\u016a\3\2\2\2w\u016c\3\2\2\2y\u016e\3")
        buf.write("\2\2\2{\u0170\3\2\2\2}\u0172\3\2\2\2\177\u0174\3\2\2\2")
        buf.write("\u0081\u017a\3\2\2\2\u0083\u0180\3\2\2\2\u0085\u0183\3")
        buf.write("\2\2\2\u0087\u0187\3\2\2\2\u0089\u019b\3\2\2\2\u008b\u019d")
        buf.write("\3\2\2\2\u008d\u01a1\3\2\2\2\u008f\u01a5\3\2\2\2\u0091")
        buf.write("\u01ac\3\2\2\2\u0093\u0094\7=\2\2\u0094\4\3\2\2\2\u0095")
        buf.write("\u0096\7-\2\2\u0096\u0097\7?\2\2\u0097\6\3\2\2\2\u0098")
        buf.write("\u0099\7/\2\2\u0099\u009a\7?\2\2\u009a\b\3\2\2\2\u009b")
        buf.write("\u009c\7,\2\2\u009c\u009d\7?\2\2\u009d\n\3\2\2\2\u009e")
        buf.write("\u009f\7B\2\2\u009f\u00a0\7?\2\2\u00a0\f\3\2\2\2\u00a1")
        buf.write("\u00a2\7\61\2\2\u00a2\u00a3\7?\2\2\u00a3\16\3\2\2\2\u00a4")
        buf.write("\u00a5\7\'\2\2\u00a5\u00a6\7?\2\2\u00a6\20\3\2\2\2\u00a7")
        buf.write("\u00a8\7(\2\2\u00a8\u00a9\7?\2\2\u00a9\22\3\2\2\2\u00aa")
        buf.write("\u00ab\7~\2\2\u00ab\u00ac\7?\2\2\u00ac\24\3\2\2\2\u00ad")
        buf.write("\u00ae\7`\2\2\u00ae\u00af\7?\2\2\u00af\26\3\2\2\2\u00b0")
        buf.write("\u00b1\7>\2\2\u00b1\u00b2\7>\2\2\u00b2\u00b3\7?\2\2\u00b3")
        buf.write("\30\3\2\2\2\u00b4\u00b5\7@\2\2\u00b5\u00b6\7@\2\2\u00b6")
        buf.write("\u00b7\7?\2\2\u00b7\32\3\2\2\2\u00b8\u00b9\7,\2\2\u00b9")
        buf.write("\u00ba\7,\2\2\u00ba\u00bb\7?\2\2\u00bb\34\3\2\2\2\u00bc")
        buf.write("\u00bd\7\61\2\2\u00bd\u00be\7\61\2\2\u00be\u00bf\7?\2")
        buf.write("\2\u00bf\36\3\2\2\2\u00c0\u00c1\7/\2\2\u00c1\u00c2\7@")
        buf.write("\2\2\u00c2 \3\2\2\2\u00c3\u00c4\5M\'\2\u00c4\"\3\2\2\2")
        buf.write("\u00c5\u00c6\5O(\2\u00c6$\3\2\2\2\u00c7\u00c8\7f\2\2\u00c8")
        buf.write("\u00c9\7g\2\2\u00c9\u00ca\7h\2\2\u00ca&\3\2\2\2\u00cb")
        buf.write("\u00cc\7t\2\2\u00cc\u00cd\7g\2\2\u00cd\u00ce\7v\2\2\u00ce")
        buf.write("\u00cf\7w\2\2\u00cf\u00d0\7t\2\2\u00d0\u00d1\7p\2\2\u00d1")
        buf.write("(\3\2\2\2\u00d2\u00d3\7k\2\2\u00d3\u00d4\7h\2\2\u00d4")
        buf.write("*\3\2\2\2\u00d5\u00d6\7g\2\2\u00d6\u00d7\7n\2\2\u00d7")
        buf.write("\u00d8\7k\2\2\u00d8\u00d9\7h\2\2\u00d9,\3\2\2\2\u00da")
        buf.write("\u00db\7g\2\2\u00db\u00dc\7n\2\2\u00dc\u00dd\7u\2\2\u00dd")
        buf.write("\u00de\7g\2\2\u00de.\3\2\2\2\u00df\u00e0\7y\2\2\u00e0")
        buf.write("\u00e1\7j\2\2\u00e1\u00e2\7k\2\2\u00e2\u00e3\7n\2\2\u00e3")
        buf.write("\u00e4\7g\2\2\u00e4\60\3\2\2\2\u00e5\u00e6\7h\2\2\u00e6")
        buf.write("\u00e7\7q\2\2\u00e7\u00e8\7t\2\2\u00e8\62\3\2\2\2\u00e9")
        buf.write("\u00ea\7k\2\2\u00ea\u00eb\7p\2\2\u00eb\64\3\2\2\2\u00ec")
        buf.write("\u00ed\7q\2\2\u00ed\u00ee\7t\2\2\u00ee\66\3\2\2\2\u00ef")
        buf.write("\u00f0\7c\2\2\u00f0\u00f1\7p\2\2\u00f1\u00f2\7f\2\2\u00f2")
        buf.write("8\3\2\2\2\u00f3\u00f4\7p\2\2\u00f4\u00f5\7q\2\2\u00f5")
        buf.write("\u00f6\7v\2\2\u00f6:\3\2\2\2\u00f7\u00f8\7k\2\2\u00f8")
        buf.write("\u00f9\7u\2\2\u00f9<\3\2\2\2\u00fa\u00fb\7P\2\2\u00fb")
        buf.write("\u00fc\7q\2\2\u00fc\u00fd\7p\2\2\u00fd\u00fe\7g\2\2\u00fe")
        buf.write(">\3\2\2\2\u00ff\u0100\7V\2\2\u0100\u0101\7t\2\2\u0101")
        buf.write("\u0102\7w\2\2\u0102\u0103\7g\2\2\u0103@\3\2\2\2\u0104")
        buf.write("\u0105\7H\2\2\u0105\u0106\7c\2\2\u0106\u0107\7n\2\2\u0107")
        buf.write("\u0108\7u\2\2\u0108\u0109\7g\2\2\u0109B\3\2\2\2\u010a")
        buf.write("\u010b\7r\2\2\u010b\u010c\7c\2\2\u010c\u010d\7u\2\2\u010d")
        buf.write("\u010e\7u\2\2\u010eD\3\2\2\2\u010f\u0110\7e\2\2\u0110")
        buf.write("\u0111\7q\2\2\u0111\u0112\7p\2\2\u0112\u0113\7v\2\2\u0113")
        buf.write("\u0114\7k\2\2\u0114\u0115\7p\2\2\u0115\u0116\7w\2\2\u0116")
        buf.write("\u0117\7g\2\2\u0117F\3\2\2\2\u0118\u0119\7d\2\2\u0119")
        buf.write("\u011a\7t\2\2\u011a\u011b\7g\2\2\u011b\u011c\7c\2\2\u011c")
        buf.write("\u011d\7m\2\2\u011dH\3\2\2\2\u011e\u011f\6%\2\2\u011f")
        buf.write("\u0129\5\u008dG\2\u0120\u0121\7\17\2\2\u0121\u0124\7\f")
        buf.write("\2\2\u0122\u0124\t\2\2\2\u0123\u0120\3\2\2\2\u0123\u0122")
        buf.write("\3\2\2\2\u0124\u0126\3\2\2\2\u0125\u0127\5\u008dG\2\u0126")
        buf.write("\u0125\3\2\2\2\u0126\u0127\3\2\2\2\u0127\u0129\3\2\2\2")
        buf.write("\u0128\u011e\3\2\2\2\u0128\u0123\3\2\2\2\u0129\u012a\3")
        buf.write("\2\2\2\u012a\u012b\b%\2\2\u012bJ\3\2\2\2\u012c\u0130\5")
        buf.write("\u0085C\2\u012d\u012f\5\u0087D\2\u012e\u012d\3\2\2\2\u012f")
        buf.write("\u0132\3\2\2\2\u0130\u012e\3\2\2\2\u0130\u0131\3\2\2\2")
        buf.write("\u0131L\3\2\2\2\u0132\u0130\3\2\2\2\u0133\u0135\t\3\2")
        buf.write("\2\u0134\u0133\3\2\2\2\u0134\u0135\3\2\2\2\u0135\u0136")
        buf.write("\3\2\2\2\u0136\u0137\5\u0089E\2\u0137N\3\2\2\2\u0138\u013c")
        buf.write("\t\4\2\2\u0139\u013b\t\5\2\2\u013a\u0139\3\2\2\2\u013b")
        buf.write("\u013e\3\2\2\2\u013c\u013a\3\2\2\2\u013c\u013d\3\2\2\2")
        buf.write("\u013d\u0141\3\2\2\2\u013e\u013c\3\2\2\2\u013f\u0141\t")
        buf.write("\6\2\2\u0140\u0138\3\2\2\2\u0140\u013f\3\2\2\2\u0141P")
        buf.write("\3\2\2\2\u0142\u0143\7\60\2\2\u0143R\3\2\2\2\u0144\u0145")
        buf.write("\7,\2\2\u0145T\3\2\2\2\u0146\u0147\7*\2\2\u0147V\3\2\2")
        buf.write("\2\u0148\u0149\7+\2\2\u0149X\3\2\2\2\u014a\u014b\7.\2")
        buf.write("\2\u014bZ\3\2\2\2\u014c\u014d\7<\2\2\u014d\\\3\2\2\2\u014e")
        buf.write("\u014f\7?\2\2\u014f^\3\2\2\2\u0150\u0151\7]\2\2\u0151")
        buf.write("`\3\2\2\2\u0152\u0153\7_\2\2\u0153b\3\2\2\2\u0154\u0155")
        buf.write("\7~\2\2\u0155d\3\2\2\2\u0156\u0157\7`\2\2\u0157f\3\2\2")
        buf.write("\2\u0158\u0159\7(\2\2\u0159h\3\2\2\2\u015a\u015b\7>\2")
        buf.write("\2\u015bj\3\2\2\2\u015c\u015d\7@\2\2\u015dl\3\2\2\2\u015e")
        buf.write("\u015f\7?\2\2\u015f\u0160\7?\2\2\u0160n\3\2\2\2\u0161")
        buf.write("\u0162\7@\2\2\u0162\u0163\7?\2\2\u0163p\3\2\2\2\u0164")
        buf.write("\u0165\7>\2\2\u0165\u0166\7?\2\2\u0166r\3\2\2\2\u0167")
        buf.write("\u0168\7#\2\2\u0168\u0169\7?\2\2\u0169t\3\2\2\2\u016a")
        buf.write("\u016b\7-\2\2\u016bv\3\2\2\2\u016c\u016d\7/\2\2\u016d")
        buf.write("x\3\2\2\2\u016e\u016f\7\61\2\2\u016fz\3\2\2\2\u0170\u0171")
        buf.write("\7\'\2\2\u0171|\3\2\2\2\u0172\u0173\7\u0080\2\2\u0173")
        buf.write("~\3\2\2\2\u0174\u0175\7,\2\2\u0175\u0176\7,\2\2\u0176")
        buf.write("\u0080\3\2\2\2\u0177\u017b\5\u008dG\2\u0178\u017b\5\u008f")
        buf.write("H\2\u0179\u017b\5\u0091I\2\u017a\u0177\3\2\2\2\u017a\u0178")
        buf.write("\3\2\2\2\u017a\u0179\3\2\2\2\u017b\u017c\3\2\2\2\u017c")
        buf.write("\u017a\3\2\2\2\u017c\u017d\3\2\2\2\u017d\u017e\3\2\2\2")
        buf.write("\u017e\u017f\bA\3\2\u017f\u0082\3\2\2\2\u0180\u0181\13")
        buf.write("\2\2\2\u0181\u0084\3\2\2\2\u0182\u0184\t\7\2\2\u0183\u0182")
        buf.write("\3\2\2\2\u0184\u0086\3\2\2\2\u0185\u0188\5\u0085C\2\u0186")
        buf.write("\u0188\t\5\2\2\u0187\u0185\3\2\2\2\u0187\u0186\3\2\2\2")
        buf.write("\u0188\u0088\3\2\2\2\u0189\u018e\7)\2\2\u018a\u018d\5")
        buf.write("\u008bF\2\u018b\u018d\n\b\2\2\u018c\u018a\3\2\2\2\u018c")
        buf.write("\u018b\3\2\2\2\u018d\u0190\3\2\2\2\u018e\u018c\3\2\2\2")
        buf.write("\u018e\u018f\3\2\2\2\u018f\u0191\3\2\2\2\u0190\u018e\3")
        buf.write("\2\2\2\u0191\u019c\7)\2\2\u0192\u0197\7$\2\2\u0193\u0196")
        buf.write("\5\u008bF\2\u0194\u0196\n\b\2\2\u0195\u0193\3\2\2\2\u0195")
        buf.write("\u0194\3\2\2\2\u0196\u0199\3\2\2\2\u0197\u0195\3\2\2\2")
        buf.write("\u0197\u0198\3\2\2\2\u0198\u019a\3\2\2\2\u0199\u0197\3")
        buf.write("\2\2\2\u019a\u019c\7$\2\2\u019b\u0189\3\2\2\2\u019b\u0192")
        buf.write("\3\2\2\2\u019c\u008a\3\2\2\2\u019d\u019e\7^\2\2\u019e")
        buf.write("\u019f\13\2\2\2\u019f\u008c\3\2\2\2\u01a0\u01a2\t\t\2")
        buf.write("\2\u01a1\u01a0\3\2\2\2\u01a2\u01a3\3\2\2\2\u01a3\u01a1")
        buf.write("\3\2\2\2\u01a3\u01a4\3\2\2\2\u01a4\u008e\3\2\2\2\u01a5")
        buf.write("\u01a9\7%\2\2\u01a6\u01a8\n\2\2\2\u01a7\u01a6\3\2\2\2")
        buf.write("\u01a8\u01ab\3\2\2\2\u01a9\u01a7\3\2\2\2\u01a9\u01aa\3")
        buf.write("\2\2\2\u01aa\u0090\3\2\2\2\u01ab\u01a9\3\2\2\2\u01ac\u01ae")
        buf.write("\7^\2\2\u01ad\u01af\5\u008dG\2\u01ae\u01ad\3\2\2\2\u01ae")
        buf.write("\u01af\3\2\2\2\u01af\u01b5\3\2\2\2\u01b0\u01b2\7\17\2")
        buf.write("\2\u01b1\u01b0\3\2\2\2\u01b1\u01b2\3\2\2\2\u01b2\u01b3")
        buf.write("\3\2\2\2\u01b3\u01b6\7\f\2\2\u01b4\u01b6\4\16\17\2\u01b5")
        buf.write("\u01b1\3\2\2\2\u01b5\u01b4\3\2\2\2\u01b6\u0092\3\2\2\2")
        buf.write("\30\2\u0123\u0126\u0128\u0130\u0134\u013c\u0140\u017a")
        buf.write("\u017c\u0183\u0187\u018c\u018e\u0195\u0197\u019b\u01a3")
        buf.write("\u01a9\u01ae\u01b1\u01b5\4\3%\2\b\2\2")
        return buf.getvalue()


class Python3Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    STRING = 16
    NUMBER = 17
    DEF = 18
    RETURN = 19
    IF = 20
    ELIF = 21
    ELSE = 22
    WHILE = 23
    FOR = 24
    IN = 25
    OR = 26
    AND = 27
    NOT = 28
    IS = 29
    NONE = 30
    TRUE = 31
    FALSE = 32
    PASS = 33
    CONTINUE = 34
    BREAK = 35
    NEWLINE = 36
    NAME = 37
    STRING_LITERAL = 38
    DECIMAL_INTEGER = 39
    DOT = 40
    STAR = 41
    OPEN_PAREN = 42
    CLOSE_PAREN = 43
    COMMA = 44
    COLON = 45
    ASSIGN = 46
    OPEN_BRACK = 47
    CLOSE_BRACK = 48
    OR_OP = 49
    XOR = 50
    AND_OP = 51
    LESS_THAN = 52
    GREATER_THAN = 53
    EQUALS = 54
    GT_EQ = 55
    LT_EQ = 56
    NOT_EQ = 57
    ADD = 58
    SUB = 59
    DIV = 60
    MOD = 61
    NOT_OP = 62
    POWER = 63
    SKIP_ = 64
    UNKNOWN_CHAR = 65

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "'+='", "'-='", "'*='", "'@='", "'/='", "'%='", "'&='", 
            "'|='", "'^='", "'<<='", "'>>='", "'**='", "'//='", "'->'", 
            "'def'", "'return'", "'if'", "'elif'", "'else'", "'while'", 
            "'for'", "'in'", "'or'", "'and'", "'not'", "'is'", "'None'", 
            "'True'", "'False'", "'pass'", "'continue'", "'break'", "'.'", 
            "'*'", "'('", "')'", "','", "':'", "'='", "'['", "']'", "'|'", 
            "'^'", "'&'", "'<'", "'>'", "'=='", "'>='", "'<='", "'!='", 
            "'+'", "'-'", "'/'", "'%'", "'~'", "'**'" ]

    symbolicNames = [ "<INVALID>",
            "STRING", "NUMBER", "DEF", "RETURN", "IF", "ELIF", "ELSE", "WHILE", 
            "FOR", "IN", "OR", "AND", "NOT", "IS", "NONE", "TRUE", "FALSE", 
            "PASS", "CONTINUE", "BREAK", "NEWLINE", "NAME", "STRING_LITERAL", 
            "DECIMAL_INTEGER", "DOT", "STAR", "OPEN_PAREN", "CLOSE_PAREN", 
            "COMMA", "COLON", "ASSIGN", "OPEN_BRACK", "CLOSE_BRACK", "OR_OP", 
            "XOR", "AND_OP", "LESS_THAN", "GREATER_THAN", "EQUALS", "GT_EQ", 
            "LT_EQ", "NOT_EQ", "ADD", "SUB", "DIV", "MOD", "NOT_OP", "POWER", 
            "SKIP_", "UNKNOWN_CHAR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "STRING", "NUMBER", "DEF", "RETURN", "IF", "ELIF", 
                  "ELSE", "WHILE", "FOR", "IN", "OR", "AND", "NOT", "IS", 
                  "NONE", "TRUE", "FALSE", "PASS", "CONTINUE", "BREAK", 
                  "NEWLINE", "NAME", "STRING_LITERAL", "DECIMAL_INTEGER", 
                  "DOT", "STAR", "OPEN_PAREN", "CLOSE_PAREN", "COMMA", "COLON", 
                  "ASSIGN", "OPEN_BRACK", "CLOSE_BRACK", "OR_OP", "XOR", 
                  "AND_OP", "LESS_THAN", "GREATER_THAN", "EQUALS", "GT_EQ", 
                  "LT_EQ", "NOT_EQ", "ADD", "SUB", "DIV", "MOD", "NOT_OP", 
                  "POWER", "SKIP_", "UNKNOWN_CHAR", "ID_START", "ID_CONTINUE", 
                  "SHORT_STRING", "STRING_NEXTLINE", "SPACES", "COMMENT", 
                  "LINE_JOINING" ]

    grammarFileName = "Python3.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


        self.lastToken = None
        self.tokens = []
        self.indentStack = []

    def emit(self,t=None):
        if t == None :
            s = self._factory.create(self._tokenFactorySourcePair, self._type, self._text, self._channel, self._tokenStartCharIndex,
                                     self.getCharIndex()-1, self._tokenStartLine, self._tokenStartColumn)
            self.emitToken(s)
            self.tokens.append(s)
            return s
        else:
            self.emitToken(t)
            self.tokens.append(t)
            return t

    def commonToken(self,type,text):
        stop = self.getCharIndex()-1
        if len(text)==0 :
            start = stop
        else:
            start = stop - len(text)+1
        return CommonToken(self._tokenFactorySourcePair,type,self.DEFAULT_TOKEN_CHANNEL,start,stop)

    def createDedent(self):
        dedent = self.commonToken(Python3Parser.DEDENT,'')
        dedent.line = self.lastToken.line
        return dedent

    @staticmethod
    def getIndentationCount(spaces):
        count = 0
        for ch in spaces:
            if ch == '\t':
                count +=( 4 - (count%4))
            elif ch == ' ':
                count += 1
            else :
                pass
        return count

    def nextToken(self):
        # Check if the end-of-file is ahead and there are still some DEDENTS expected
        if(self._input.LA(1)==Token.EOF and len(self.indentStack)!=0):
            # Remove ant trailing EOF tokens from our buffer
            i = len(self.tokens)-1
            while i>= 0 :
                if(self.tokens[i].type==Token.EOF):
                    self.tokens.pop(i)
                i-=1
            # First emit an extra line break that serves as the end of the stmt
            self.emit(self.commonToken(Python3Parser.NEWLINE,'\n'))
            # Now emit as much DEDENT tokens as needed
            while len(self.indentStack)!=0 :
                self.emit(self.createDedent())
                self.indentStack.pop()
            # put the EOF back on the token stream .
            self.emit(self.commonToken(Python3Parser.EOF,'<EOF>'))
        next = super().nextToken()
        if (next.channel == Token.DEFAULT_CHANNEL):
            # Keep track of the last token on the default channel
            self.lastToken = next
        if len(self.tokens) == 0 :
            return next
        else :
            temp = self.tokens[0]
            self.tokens.pop(0)
            return temp

    def atStartOfInput(self):
        if super().getCharIndex()==0 and super().line==1 :
            return True
        else:
            return False


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[35] = self.NEWLINE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))

    def NEWLINE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                    newLine = self.text
                    for i in newLine :
                        if i == '\r' or i == '\n' or i == '\f':
                            pass
                        else:
                            newLine.replace(str(i),'')

                    spaces = self.text.replace('\r','')
                    spaces = self.text.replace('\n','')
                    spaces = self.text.replace('\f','')

                    next = self._input.LA(1)

                    if(next=='\r' or next == '\n' or next == '\f' or next == '<EOF>'):
                        self.skip()
                    else:
                        self.emit(self.commonToken(self.NEWLINE,newLine))
                        indent = self.getIndentationCount(spaces)
                        previous = 0
                        if len(self.indentStack) != 0 :
                            previous = self.indentStack.pop()
                            self.indentStack.append(previous)
                            # it is equal to indentStack.peek()
                        if indent==previous :
                            # skip indents of the same size as the present indent-size
                            self.skip()
                        elif indent > previous :
                            self.indentStack.append(indent)
                            self.emit(self.commonToken(Python3Parser.INDENT,spaces))
                        else:
                            # Possibly emit more than 1 DEDENT token
                            while len(self.indentStack)!=0 and self.indentStack[len(self.indentStack)-1]>indent:
                                self.emit(self.createDedent())
                                self.indentStack.pop()
                
     

    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates is None:
            preds = dict()
            preds[35] = self.NEWLINE_sempred
            self._predicates = preds
        pred = self._predicates.get(ruleIndex, None)
        if pred is not None:
            return pred(localctx, predIndex)
        else:
            raise Exception("No registered predicate for:" + str(ruleIndex))

    def NEWLINE_sempred(self, localctx:RuleContext, predIndex:int):
            if predIndex == 0:
                return self.atStartOfInput()
         


