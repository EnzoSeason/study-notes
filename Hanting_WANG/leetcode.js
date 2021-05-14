// 数组中移除相关数字
var removeElement = function(nums, val) {
    let j = 0
    for(let i=0; i<nums.length; i++){
        if(nums[i]!= val){
            nums[j]=nums[i]
            j += 1
        }
    }
    nums.length = j
    return j
  };
  
// 28.实现strStr()
var strStr = function(haystack, needle) {
    if(!needle.length) return 0;
    for(let i = 0, j = needle.length; i + j <= haystack.length; i++){
        if(haystack.slice(i, i+j) === needle) return i
    }
    return -1;
};

//TODO kmp算法 真的难 看懂了 写不来 再说吧


// 35搜索插入位置
var searchInsert = function(nums, target) {
    for(let i = 0; i < nums.length; i++){
        if(target<=nums[i]) return i;
    }
    return nums.length
};

// 插入位置二分
var searchInsert_2 = function(nums, target) {
    let start = 0
    let end = nums.length - 1
    while(start <= end){
        let mid = parseInt((start + end)/2)
        if(nums[mid] < target){
            start = mid + 1
        }else if(nums[mid]>target){
            end = mid -1
        }else{
            return mid
        }
    }
    return start
};

// 38 外观数列 笑死我了 评论第一 笑裂了

//53最大子序和 
var maxSubArray = function(nums) {
    let dp = [nums[0]]
    let max = dp[0]
    let len = nums.length
    for(let i = 1; i < len; i++){
        dp[i] = Math.max(dp[i-1]+nums[i], nums[i])
        max = Math.max(dp[i], max)
    }
    return max
};

var a = [1, 3, 4, 5]
var b = 2
var res = maxSubArray(a)
console.log(res)