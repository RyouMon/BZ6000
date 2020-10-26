package chapter02;

/**
 * 测试字符类型
 */
public class TestPrimitiveDataType3 {
    public static void main(String[] args) {
        char a = 'T';
        char b = '上';
        char c = '\u0061';
        System.out.println(c);

        //转义字符
        System.out.println(""+'a'+'\n'+'b');
        System.out.println(""+'a'+'\t'+'b');
        System.out.println(""+'a'+'\''+'b');

        //String就是字符序列
        String d = "abc";
    }
}
