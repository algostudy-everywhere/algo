import Foundation

func N과M2() {
    let input = readLine()!.split(separator: " ").compactMap { Int($0) }
    let N = input[0]
    let M = input[1]
    let permutation = Array(1...N)
    
    func findPermutation(k: Int, s: Int, arr: [Int]) {
        if k == M {
            print(arr.map { String($0) }.joined(separator: " "))
            return
        }

        for i in s..<N {
            var newArr = arr
            newArr.append(permutation[i])
            findPermutation(k: k + 1, s: i + 1, arr: newArr)
        }
    }
    
    findPermutation(k: 0, s: 0, arr: [])
}
