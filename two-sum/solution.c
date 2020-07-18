

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    static int a[2]={0,0},i,k;
    for(i=0;i<numsSize;i++){
        for(k=i+1;k<numsSize;k++){
            if((nums[i]+nums[k])==target){
                a[0]=i;
                a[1]=k;
                break;
            }
        }
    }
    *returnSize=2;
  return a;
}
