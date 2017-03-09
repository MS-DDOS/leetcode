object NumIslands {
	def main(args: Array[String]){
		var graph = Array(
						Array(1,1,1,0,1),
						Array(1,1,0,0,0),
						Array(1,1,0,1,1),
						Array(0,0,0,0,1),
						Array(1,1,1,0,0)
					)
		println(num_islands(graph))
	}

	def num_islands(G: Array[Array[Int]]): Int = {
		var islands = 0
		for(i <- 0 until G.length){
			for(j <- 0 until G(i).length){
				if(G(i)(j) == 1){
					islands += 1
					sink(G, i, j)
				}		
			}
		}
		islands
	}

	def sink(G: Array[Array[Int]], i: Int, j: Int): Unit = {
		try {
			G(i)(j) match {
				case 1 => G(i)(j) = 0; sink(G, i+1, j); sink(G, i-1, j); sink(G, i, j+1); sink(G, i, j-1);
				case 0 => Unit
			}
		} catch {
			case e: ArrayIndexOutOfBoundsException => Unit
		}
	}
}