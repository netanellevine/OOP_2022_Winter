public class FuncToTest {

    /**
     * Given two strings create a new string that is a "Sewing Merge" of them
     * for example:
     * s1 = "abcd" s2="efgh"
     * The output will be "aebfcgdh"
     * The function is not fully working on purpose...
     * @param s1
     * @param s2
     * @return The "Sewed mergerd" output
     */

    public static String MySewingMerge(String s1, String s2){
        String output = "";
        int i = 0;
        while(i<s1.length()){
            output+=s1.charAt(i);
            output+=s2.charAt(i);
            i++;
        }
        return output;
    }
}


/**
 * So what's wrong with this function?
 * 1. We never checked what will happen if s1 or s2 will be empty
 * 2. We never considered the fact that we can't assume that both strings have the same
 * length.
 *      2.1. if s2 is shorter than s1 we will get NullPointerException
 *      2.2. if s2 is longer than s1 then we will not finish iterating over s1
 *
 * So let's assume the function is working on the inputs we checked(for equal sized string only)
 * We will create JUnit in order to find our mistakes and fix them
 */
