/**
 * 自定义异常
 */
public class TestDiyException {
    public static void main(String[] args) throws IllegalAgeExcepiton {
        Person person = new Person();
        person.setAge(-10);
    }
}

class Person {
    int age;

    public int getAge() {
        return age;
    }

    public void setAge(int age) throws IllegalAgeExcepiton {
        if (age < 0) {
            throw new IllegalAgeExcepiton("年龄不能为符数");
        } else {
            this.age = age;
        }
    }
}

class IllegalAgeExcepiton extends Exception {
    public IllegalAgeExcepiton() {
    }

    public IllegalAgeExcepiton(String message) {
        super(message);
    }
}
