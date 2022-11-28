import java.util.ArrayList;
import java.util.Arrays;

public class Box<T> {
    private T t;

    public void add(T t) {
        this.t = t;
    }

    public T get() {
        return t;
    }

    public static <K> void swap(K arr[], int i, int j){
        K temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }


    public static void main(String[] args) {
        Box<Integer> integerBox = new Box<>();
        Box<String> stringBox = new Box<>();

        integerBox.add(5);
        stringBox.add(new String("Hello World"));

        System.out.println(integerBox.get());
        System.out.println(stringBox.get());
        Integer[] arr = {1, 2, 3, 4, 5};
        Double[] arr2 = {1.0, 2.3, 3.2, 4.5, 5.4};
        String[] arr3 = {"A", "B", "C", "D", "E"};

        swap(arr, 0, 3);
        System.out.println(Arrays.toString(arr));
        swap(arr2, 0, 3);
        System.out.println(Arrays.toString(arr2));
        swap(arr3, 0, 3);
        System.out.println(Arrays.toString(arr3));

    }
}
