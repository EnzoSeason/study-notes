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
  
  nums = [3,2,2,3]
  val = 3
  var res = removeElement(nums, val)
  console.log(nums)
  console.log(res)