package Lesson8.FactoryAbstractFactory;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Stack;

public class ListFactory {
    public static List listFactory(String type){
        switch (type){
            case ("Stack"):{
                return new Stack();
            }
            case ("Dynamic"):{
                return new ArrayList();
            }
            case default:{
                return new LinkedList();
            }
        }
    }

    public static void main(String[] args) {
        List<String> l1 = ListFactory.listFactory("");
        List<String> l2 = ListFactory.listFactory("Dynamic");
        System.out.println(l1.getClass().getName());
        System.out.println(l2.getClass().getName());
    }
}
