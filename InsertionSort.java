import java.util.Arrays;

public class InsertionSort {

    public static void main(String[] args){

		int[] numArr = {2,3,2,4};

        for(int i = 0; i < numArr.length; i++){
            int key = numArr[i];
            int j = i-1;
            while(j >= 0 && numArr[j] > key){
                numArr[j+1] = numArr[j];
                j -= 1;
            }
            numArr[j+1] = key;
        }

        System.out.println(Arrays.toString(numArr));
	
	}
}