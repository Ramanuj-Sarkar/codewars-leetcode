/*
This implements square matrix multiplication.
*/
public class Kata {

	public static int[][] matrixMultiplication(int[][] a, int[][] b) {
    int sideLength = a.length;
    int[][] answer = new int[sideLength][sideLength];
    
    for(int ycoord = 0; ycoord < sideLength; ++ycoord) { // this is the y-coordinate of the first one
      for(int xcoord = 0; xcoord < sideLength; ++xcoord) { // this is the x-coordinate of the second one
        int yx = 0;
        for(int shifter = 0; shifter < sideLength; ++shifter) {
		  // matrix multiplication entails adding these numbers like this
          yx += a[ycoord][shifter] * b[shifter][xcoord];
        }
        answer[ycoord][xcoord] = yx;
      }
    }
		return answer;
	}
}
