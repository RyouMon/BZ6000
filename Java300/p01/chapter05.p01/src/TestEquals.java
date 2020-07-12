/**
 * 测试 equals
 */
public class TestEquals {
    public static void main(String[] args) {
        Person2 p1 = new Person2(123, "WenLiang");
        Person2 p2 = new Person2(123, "LiangWen");
        System.out.println(p1.equals(p2)); // true
        System.out.println(p1 == p2); // false
    }
}

class Person2{
    int id;
    String name;

    public Person2(int id, String name) {
        this.id = id;
        this.name = name;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Person2 person2 = (Person2) o;
        return id == person2.id;
    }
}
