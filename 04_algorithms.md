## **Алгоритмы**

### FizzBuzz <a name="simplefizzbuzz"></a>  

Почему нужно просить выполнить столь простое задание? Вот подробности — «[FizzBuzz, или почему программисты не умеют программировать](https://habr.com/ru/post/298134/)», если вкратце, то, к сожалению, можно сказать, что и профильное образование, и профильный опыт не уберегают от потери базовых навыков программирования.  

Задание: Напишите программу, которая выводит на экран числа от 1 до 100. При этом вместо чисел, кратных трем, программа должна выводить слово «Fizz», а вместо чисел, кратных пяти — слово «Buzz». Если число кратно и 3, и 5, то программа должна выводить слово «FizzBuzz».  

Самый простой вариант:  
```csharp
const int Max = 100;

for (var i = 1; i <= Max; i++)
{
   if ((i % 3 == 0) && (i % 5 == 0))
   {
      Console.WriteLine("FizzBuzz");
   }
   else if (i % 3 == 0)
   {
      Console.WriteLine("Fizz");
   }
   else if (i % 5 == 0)
   {
      Console.WriteLine("Buzz");
   }
   else
   {
      Console.WriteLine(i);
   }
}
```

или чуточку улучшенный вариант:  

```csharp
const int Max = 100;

for (var i = 1; i <= Max; i++)
{
   if (i % 3 == 0)
   {
      if (i % 5 == 0)
      {
         Console.WriteLine("FizzBuzz");
      }
      else
      {
         Console.WriteLine("Fizz");
      }
   }
   else if (i % 5 == 0)
   {
      Console.WriteLine("Buzz");
   }
   else
   {
      Console.WriteLine(i);
   }
}
```

Больше подробностей про оптимизацию задачи FizzBuzz — «[FizzBuzz по-сениорски](https://habr.com/ru/post/540136/)».  

### Пузырьковая сортировка (BubbleSort) <a name="bubblesort"></a>

Простейший алгоритм, состоит из повторяющихся проходов по сортируемому массиву. В процессе каждого прохода элементы мвссива сравниваются попарно; элементы, не удовлетворяющие условию сортировки, меняются местами.

```cs
internal static class Bubble
{
   internal static int[] Sort(int[] randomArray)
   {
      var arr = (int[])randomArray.Clone();
      var len = arr.Length;

      for (var i = 0; i < len - 1; i++)
      {
         for (var j = 0; j < len - i - 1; j++)
         {
            if (arr[j] > arr[j + 1])
            {
               (arr[j], arr[j + 1]) = (arr[j + 1], arr[j]);
            }
         }
      }

      return arr;
   }
}
```



### Быстрая сортировка (QuickSort) <a name="basicquicksort"></a>  

Идея алгоритма следующая:  
1. Выбирается опорный элемент, это в первом приближении может быть любой из элементов массива, например, из середины массива.
2. Все элементы массива сравниваются с опорным и переставляются так, чтобы образовать новый массив, состоящий из двух последовательных сегментов - элементы меньшие опорного, равные опорному + большие опорного.
3. Если длина сегментов больше 1, то рекурсивно выполнить сортировку и для них тоже.

```cs
internal static class Quick
{
   internal static int[] Sort(int[] randomArray)
   {
      var arr = (int[])randomArray.Clone();

      QuickSort(arr, 0, arr.Length - 1);

      return arr;
   }

   private static int[] QuickSort(int[] a, int i, int j)
   {
      if (i < j)
      {
         int q = Partition(a, i, j);
         a = QuickSort(a, i, q);
         a = QuickSort(a, q + 1, j);
      }
      return a;
   }

   private static int Partition(int[] a, int p, int r)
   {
      int x = a[p];
      int i = p - 1;
      int j = r + 1;
      while (true)
      {
         do
         {
            j--;
         }
         while (a[j] > x);
         do
         {
            i++;
         }
         while (a[i] < x);
         if (i < j)
         {
            int tmp = a[i];
            a[i] = a[j];
            a[j] = tmp;
         }
         else
         {
            return j;
         }
      }
   }
}
```



### Сортировка слиянием (MergeSort) <a name="basicmergesort"></a>  

Ключевым моментом сортировки слиянием является (как ни странно :) слияние двух массивов. При слиянии массивы сравниваются поэлементо и меньший элемент записывается в результирующий массив; после того, как достигнут конец одного из массивов, в результирующий массив переписывается "хвост" оставшегося массива.  
Совместно со слиянием двух массивов используется рекурсивное разбиение сортируемого массива на сегменты меньшего размера.

```cs
internal static class Merge
{
   internal static int[] Sort(int[] randomArray)
   {
      var sortedArray = (int[])randomArray.Clone();

      MergeSort(sortedArray);

      return sortedArray;
   }

   private static void MergeSort(int[] array)
   {
      var length = array.Length;

      if (length <= 1)
      {
         return;
      }

      var leftSize = length / 2;
      var rightSize = length - leftSize;
      var leftArray = new int[leftSize];
      var rightArray = new int[rightSize];

      Array.Copy(array, 0, leftArray, 0, leftSize);
      Array.Copy(array, leftSize, rightArray, 0, rightSize);

      MergeSort(leftArray);
      MergeSort(rightArray);

      Merges(array, leftArray, rightArray);
   }

   private static void Merges(int[] array, int[] leftArray, int[] rightArray)
   {
      int leftIndex = 0, rightIndex = 0, targetIndex = 0;

      var remaining = leftArray.Length + rightArray.Length;

      while (remaining > 0)
      {
         if (leftIndex >= leftArray.Length)
            array[targetIndex] = rightArray[rightIndex++];
         else if (rightIndex >= rightArray.Length)
            array[targetIndex] = leftArray[leftIndex++];
         else if (leftArray[leftIndex].CompareTo(rightArray[rightIndex]) < 0)
            array[targetIndex] = leftArray[leftIndex++];
         else
            array[targetIndex] = rightArray[rightIndex++];

         targetIndex++;
         remaining--;
      }
   }
}

```



### Пирамидальная сортировка (HeapSort) <a name="basicheapsort"></a>  

Сначала превращаем массив в двоичное дерево за О(n) операций.
Раз за разом преобразуя дерево, получим отсортированный массив.


```cs
internal static class Heap
{
   internal static int[] Sort(int[] randomArray)
   {
      var sortedArray = (int[])randomArray.Clone();

      int n = sortedArray.Length;

      // Build heap (rearrange array)
      for (int i = n / 2 - 1; i >= 0; i--)
         heapify(sortedArray, n, i);

      // One by one extract an element from heap
      for (int i = n - 1; i > 0; i--)
      {
         // Move current root to end
         int temp = sortedArray[0];
         sortedArray[0] = sortedArray[i];
         sortedArray[i] = temp;

         // call max heapify on the reduced heap
         heapify(sortedArray, i, 0);
      }

      return sortedArray;
   }

   private static void heapify(int[] arr, int n, int i)
   {
      int largest = i; // Initialize largest as root
      int l = 2 * i + 1; // left = 2*i + 1
      int r = 2 * i + 2; // right = 2*i + 2

      // If left child is larger than root
      if (l < n && arr[l] > arr[largest])
         largest = l;

      // If right child is larger than largest so far
      if (r < n && arr[r] > arr[largest])
         largest = r;

      // If largest is not root
      if (largest != i)
      {
         int swap = arr[i];
         arr[i] = arr[largest];
         arr[largest] = swap;

         // Recursively heapify the affected sub-tree
         heapify(arr, n, largest);
      }
   }
}
```



### Сортировка вставками (InsertionSort) <a name="basicinsertionsort"></a>  

Каждый новый элемент заносится в выходную последовательность "индивидуально", т. е. каждый раз для добавления нового элемента приходится сдвигать часть массива. Алгоритм медленный, для ускорения вставки можно использовать бинарный поиск.

```cs
internal static class Insertion
{
   internal static int[] Sort(int[] randomArray)
   {
      var sortedArray = (int[])randomArray.Clone();

      int n = sortedArray.Length;
      for (int i = 1; i < n; ++i)
      {
         int key = sortedArray[i];
         int j = i - 1;

         // Move elements of arr[0..i-1],
         // that are greater than key,
         // to one position ahead of
         // their current position
         while (j >= 0 && sortedArray[j] > key)
         {
            sortedArray[j + 1] = sortedArray[j];
            j = j - 1;
         }
         sortedArray[j + 1] = key;
      }

      return sortedArray;
   }
}
```



### Timsort <a name="basictimsort"></a>  

Комбинированный алгоритм сортировки, сочетающий сортировку вставками и сортировку слиянием. Стандарт для Python, Java, Swift



### Introsort <a name="basicintrosort"></a>  

Комбинированный алгоритм сортировки, использует быструю сортировку, плюс, при превышении глубины рекурсии некоторой величины (например, логарифма от числа сортируемых элементов), переключается на пирамидальную сортировку.



### Поразрядная сортировка (RadixSort) <a name="basicradixsort"></a>  

Сортирует только сущности, которые можно разбить на "разряды", имеющие разный вес. Это могут быть, например, целые числа или строки. Соответсвенно, элементы сортируются поразрядно, начиная с разряда, имеющего максимальный вес.

```cs
internal static class Radix
{
   internal static int[] Sort(int[] randomArray)
   {
      var sortedArray = (int[])randomArray.Clone();

      int i, j;
      int[] tmp = new int[sortedArray.Length];
      for (int shift = 31; shift > -1; --shift)
      {
         j = 0;
         for (i = 0; i < sortedArray.Length; ++i)
         {
            bool move = (sortedArray[i] << shift) >= 0;
            if (shift == 0 ? !move : move)
               sortedArray[i - j] = sortedArray[i];
            else
               tmp[j++] = sortedArray[i];
         }
         Array.Copy(tmp, 0, sortedArray, sortedArray.Length - j, j);
      }

      return sortedArray;
   }
}
```



### Таблица сравнения методов сортировки <a name="basicsortingcomparisontable"></a>  
  
<style>
table th:first-of-type {
    width: 35%;
}
table th:nth-of-type(2) {
    width: 35%;
}
table th:nth-of-type(3) {
    width: 5%;
}
table th:nth-of-type(4) {
    width: 5%;
}
table th:nth-of-type(5) {
    width: 5%;
}
table th:nth-of-type(6) {
    width: 5%;
}
table th:nth-of-type(7) {
    width: 5%;
}
table th:nth-of-type(8) {
    width: 5%;
}
</style>

| Сортировка | Преимущество | Best | Avg | Worst | Mem | Stable | Paral |
| :- | :- | :-: | :-: | :-: | :-: | :-: | :-: |
| Пузырьковая<br>(Bubble) | Простейшая реализация | n | n^2 | n^2 | 1 | + | + |
| Быстрая<br>(Quick) | Хорошее быстродействие в среднем случае | n*logn | n*logn | n^2 | logn | +/-<br>(depends) | + |
| Слиянием<br>(Merge) | Может работать со структурами, к которым возможен только последовательный доступ | n*logn | n*logn | n*logn | n<br>(depends) | + | + |
| Пирамидальная<br>(Heap) | Предсказуемая производительность в наихудшем случае, рекомедуется для почти отсортированных данных | n*logn | n*logn | n*logn | 1 | - | - |
| Вставками<br>(Insertion) | Рекомедуется для почти отсортированных данных или для малого количества элементов | n | n^2 | n^2 | 1 | + | - |
| Timsort | Комбинированный алгоритм. Стандарт для Python, Java, Swift | n*logn | n*logn | n*logn | logn | - | - |
| Introsort | Комбинированный алгоритм. Стандарт для .Net | n*logn | n*logn | n*logn | logn | - | - |
| Поразрядная<br>(Radix) | Быстрая сортировка для целых чисел и строк | n*w | n*w | n*w | n+w | +/-<br>(depends) | + |

### Линейный поиск <a name="basiclinearsearch"></a>  

Последовательный поиск элемента в неосортированном массиве



### Бинарный поиск <a name="basicbinarysearch"></a>  

Берется значение из середины отсортрованного массива и сравнивается с искомой величиной. В завистмости от сравнения дальнейший рекурсивный поиск продолжается в середине либо левого, либо правого подмассива.



### Поиск в глубину (DFS) <a name="basicdfs"></a>  

Метод обхода графа. Depth-first search (DFS) можно чуть точнее перевести как "поиск в первую очередь в глубину". Соответственно, рекурсивный алгоритм поиска идет «вглубь» графа, насколько это возможно. Есть нерекурсивные варианты алгоритма, разгружающие стек вызовов.



### Поиск в ширину (BFS) <a name="basicbfs"></a>  

В отличие от предыдущего варианта алгоритм Breadth-first search (BFS) перебирает в первую очередь вершины с одинаковым расстоянием от корня, и только потом идет «вглубь».



### Алгоритм Дейкстры <a name="basicdijkstras"></a>  

Находит кратчайшие пути от одной из вершин графа до всех остальных. Алгоритм работает только для графов без отрицательных рёбер.



### Алгоритм Беллмана-Форда <a name="basicbellmanford"></a>  

Как и алгоритм Дейкстры, находит кратчайшие пути от одной из вершин графа до всех остальных, но, в отличие от первого, позволяет работать с графами с ребрами, имеющими отрицательный вес.



### Таблица сравнения методов поиска <a name="basicfindingcomparisontable"></a>  

| Вид поиска | Структура данных | Avg | Worst | Mem |
| :- | :- | :-: | :-: | :-: |
| Линейный поиск | Массив | n | n | 1 |
| Бинарный поиск | Отсортированный массив | logn | n | 1 |
| Поиск в глубину (DFS) | Граф |  | V+E | V |
| Поиск в ширину (BFS) | Граф |  | V+E | V |
| Алгоритм Дейкстры | Граф | (V+E)logV | (V+E)logV | V |
| Алгоритм Беллмана-Форда | Граф | V*E | V*E | V |



### Матрица смежности <a name="basicgraphadjacencymatrix"></a>  

Квадратная целочисленная матрица размера V*V, в которой значение элемента a{i,j} равно числу рёбер из i-й вершины в j-ю вершину.  
Матрица смежности простого графа (не содержащего петель и кратных рёбер) является бинарной матрицей и содержит нули на главной диагонали.



### Матрица инцидентности <a name="basicgraphincidencematrix"></a>  

Способ представления графа, в которой указываются связи между инцидентными элементами графа (ребрами и вершинами). Столбцы матрицы соответствуют ребрам, строки — вершинам. Ненулевое значение в ячейке матрицы указывает связь между вершиной и ребром (их инцидентность). Если связи между вершиной и ребром нет, то в соответствующую ячейку ставится «0».  
В случае ориентированного графа каждой дуге ставится в соответствующем столбце: 1 в строке вершины x и -1 в строке вершины y.  



### Список смежности <a name="basicgraphadjacencylist"></a>  

Способ представления графа в виде коллекции списков вершин. Каждой вершине графа соответствует список, состоящий из «соседей» этой вершины.  
Варианты:  
• использование хеш-таблицы для ассоциации каждой вершины со списком смежных вершин;
• вершины представлены числовым индексом в массиве, каждая ячейка массива ссылается на однонаправленный связанный список соседних вершин;  
• специальные классы вершин и рёбер, каждый объект вершины содержит ссылку на коллекцию рёбер, каждый объект ребра содержит ссылки на исходящую и входящую вершины.



### Список инцидентности <a name="basicgraphincidencelist"></a>  

Список инцидентности похож на список смежности, только с той разницей, что в i-ой строке записываются номера ребер, инцидентных данной i-ой вершине.



### Сравнение структур представления графов <a name="basicgraphstructcomparison"></a>  

| Метод | Mem | Add V | Add E | Remove V | Remove E | Проверка смежн. V |
| :- | :-: | :-: | :-: | :-: | :-: | :-: |
| Матрица смежности<br>(Adjacency matrix) | V^2 | V^2 | 1 | V^2 | 1 | 1 |
| Матрица инцидентности<br>(Incidence matrix) | V*E | V*E | V*E | V*E | V*E | E |
| Список смежности<br>(Adjacency list) | V+E | 1 | 1 | V+E | E | V |
| Список инцидентности<br>(Incidence list) | V+E | 1 | 1 | E | E | E |

### О-о-о! Большое! <a name="basicbigo"></a>  

Нотация O - характеристика асимптотической сложности алгоритма без учета константы.  

n! >> 2^n >> n^3 >> n^2 >> nlogn >> n >> logn >> 1

### P vs NP <a name="advancedalgorithmspvsnp"></a>  

Задачи класса P — реально вычислимые задачи ([тезис Кобэма](https://en.wikipedia.org/wiki/Cobham%27s_thesis)), решаются за полиномиальное время.  
NP-полные задачи —  не разрешимы за полиномиальное время, но могут быть сведены к задачам разрешимости (да/нет), которые, в свою очередь, решаются за полиномиальное время.

Источники!!!
