#include <stdio.h>
#include <string.h>
#include <Windows.h>

void FileEncoding()

{

	FILE * FileCreat=NULL;
	int File;
	char KEY[] = "Encryted Jalnik's File KKKKKKK";
	char *Type;
	int KEY_LEN = strlen(KEY);
	getchar();
	for(;;)
	{
		Type = "sample.png";
		FileCreat=fopen(Type,"rb");
		if(FileCreat==NULL)
		{
			printf("\n파일이 존재하지 않습니다.\n");

			exit(0);

		}
		else
		{
			FILE * CreatFile;
			char *NameType;
			NameType = "sample_en.png";
			CreatFile=fopen(NameType,"wb");
			int cnt = 0;
			
			while ( (File = fgetc(FileCreat)) != EOF ) 
			{
				File^=KEY[cnt % KEY_LEN];
				printf(".");
				fputc(File,CreatFile);
				cnt+=1;
			}
			
			fclose(CreatFile);
			break;
		}
	}
	fclose(FileCreat);
}

int main(){
	printf("HAHA!!! Jalnik, your file is Encryted!!!\n");
	FileEncoding();
	printf("Perfect!");
	return 0;
}
