package design_patterns_java.Adapter;

public class OrderButton implements Drinkable {
    private BeerBottle bottle;

    @Override
    public void orderBeer() {
        bottle.getBeerFromBottle();
    }
}
