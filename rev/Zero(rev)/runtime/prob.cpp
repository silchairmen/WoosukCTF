# include <stdio.h>
# include <string.h>

int check(char c){
	if(c == 70){
		return 1;
	}
	return 0;
}

int genKey(char k){
	if(check(k)){
		return (k ^ 70); 
	}
	else{
	    k -= 32; // 1단계
	    k = (k - 22 + 95) % 95; // 2단계 및 3단계, 95를 더해 음수를 방지
	    return k + 32; // 4단계
	}
}

char encrypt(char a, char b){
	return a + b;
}

int main(){
	unsigned char key[21] = "ue~uo&,u}Fju+~HuaH0u";
	unsigned char flag[] = "_this_is_sample_flag_";
	unsigned char dec_key[21]={0,};
	
	int k_len = strlen((const char*)key);
	
	printf("Key Gen....\n");
	for(int i = 0; i < k_len; i++){
		dec_key[i] = genKey(key[i]);
	}
	
	int len = strlen((const char*)dec_key);
	int f_len = strlen((const char*)flag);
	
	printf("Encrypt....\n");
	for (int j = 0; j < len; j++){
		for(int i = 0; i < f_len; i++){
			flag[i] = encrypt(dec_key[j%len], flag[i]);
		}
	}
	
	printf("Write File....\n");
	FILE * CreatFile;
	char *NameType;
	NameType = "sample.txt";
	CreatFile=fopen(NameType,"wb");
	int cnt = 0;
	
	while (cnt < strlen((const char*)flag))
	{
		fprintf(CreatFile, "%x", flag[cnt]);
		cnt+=1;
	}
	
	fclose(CreatFile);
}
