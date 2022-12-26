package design_patterns_java.FactoryAbstractFactory;

import java.util.Collections;
import java.util.Scanner;

public class CollectionAbstractFactory {
    public Collections produceCollection(String type){
        Scanner sc = new Scanner(System.in);

        switch(type){
            case ("List"): {
                System.out.println("Enter the type of list you want:");
                System.out.println("Options: Stack, Dynamic, and for linked list enter anything else");
                String input = sc.nextLine();
                return (Collections) ListFactory.listFactory(input);
            }
            case ("Set"):{
                System.out.println("Enter the number of elements you want:");
                int input = sc.nextInt();
                return (Collections) SetFactory.setFactoryMethod(input);
            }
            case ("Map"):{
                System.out.println("Enter the number of elements you want:");
                int input = sc.nextInt();
                return (Collections) MapFactory.mapFactoryMethod(input);
            }

        }
        return null;
    }
}
