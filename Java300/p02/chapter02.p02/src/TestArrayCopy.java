/**
 * 测试数组的拷贝
 */
public class TestArrayCopy {
    public static void main(String[] args) {
        String[] s1 = {"a", "b", "c", "d", "e"};
        String[] s2 = extendRange(s1);
        for (String each:s2){
            System.out.println(each);
        }

    }

    public static void testCopy(){
        String[] s1 = {"a", "b", "c", "d", "e"};
        String[] s2 = new String[5];
        System.arraycopy(s1, 1, s2, 0, 3);
        for (String each:s2) {
            System.out.println(each);
        }
    }
    // 从数组中删除一个元素（本质上是数组的拷贝）
    public static String[] removeElment(String[] str, int index) {
        System.arraycopy(str, index+1, str, index, str.length-(index+1));
        str[str.length-1] = null;
        return str;
    }
    // 扩展一个数组（本质上也是数组的拷贝）
    public static String[] extendRange(String[] str) {
        String[] newstr = new String[str.length+10];
        System.arraycopy(str, 0, newstr, 0, str.length);
        return newstr;
    }
}
