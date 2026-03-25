public class Kata {

	public static int[][] matrixMultiplication(int[][] a, int[][] b) {
    int sideLength = a.length;
    int[][] answer = new int[sideLength][sideLength];
    
    for(int ycoord = 0; ycoord < sideLength; ++ycoord) {
      for(int xcoord = 0; xcoord < sideLength; ++xcoord) {
        int yx = 0;
        for(int shifter = 0; shifter < sideLength; ++shifter) {
          yx += a[ycoord][shifter] * b[shifter][xcoord];
        }
        answer[ycoord][xcoord] = yx;
      }
    }
		return answer;
	}
}
