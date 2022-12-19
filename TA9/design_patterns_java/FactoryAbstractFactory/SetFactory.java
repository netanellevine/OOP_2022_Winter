package Lesson8.FactoryAbstractFactory;

import java.util.*;

/**
 * Will solve the same problem as MapFactory
 */

public class SetFactory {
    private static int k=10000000;
    public static Set setFactoryMethod(int element){
        if(element < k){
            return new HashSet();
        }
        else{
            return new TreeSet();
        }
    }
}
