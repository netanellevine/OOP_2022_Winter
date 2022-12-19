package design_patterns_java.FactoryAbstractFactory;

import java.util.HashMap;
import java.util.Map;
import java.util.TreeMap;

/**
 * Let's review what we know about maps in java.
 * HashMap: each action will take O(1) running time but the amortized time will be O(n).
 * Which means if we will have alot of elements in the map it might not be as fast as we want it to be.
 *
 * TreeMap: each action will take O(logn) running time.
 * Which means if we will have few elements it might be slower than HashMap, but if we have alot of
 * elements, it might be faster than HashMap.
 *
 * Now let's define a limit k and create a factory method of maps according to the following algorith:
 * 1.   n = the number of estimated elements.
 * 2.   if n < k -> Which mean we won't cross the limit
 * 3.       return HashMap
 * 4.   else
 * 5.       return TreeMap
 */

public class MapFactory {
    private static int k=10000000;
    public static Map mapFactoryMethod(int element){
        if(element < k){
            return new HashMap();
        }
        else{
            return new TreeMap();
        }
    }

    public static void main(String[] args) {
        Map<Integer, String> map1 = MapFactory.mapFactoryMethod(1500);
        Map<Integer, String> map2 = MapFactory.mapFactoryMethod(1500000000);
        System.out.println(map1.getClass().getName());
        System.out.println(map2.getClass().getName());
    }
}
