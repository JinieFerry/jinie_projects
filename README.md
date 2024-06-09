# Abstarct
0. jinie_project_pc폴더는 Vscode Git Hub연동 에러를 피하기 위해 초기 단계로 돌아온 폴더, jinie_projects Repository와 연동되어있는 상태.
1. instant_jinie_voice_4는 ~3와 같은 코드를 초석으로 수정해나가는 코드.
2-1. jinie_projects Repository는 instant_jinie_voice를 기반으로 하는 프로젝트를 전개하는 곳. 
2-2. 다른 Repository들과의 차이는 연동 에러 해결 전 후로 구분할 수 있다.

# Error History
## Error-1 : git pull and push error (fixed)
### study 
1)생활코딩 visual code로 다루는 git < 코드 시간여행의 원리
https://www.youtube.com/watch?v=yc0rxkt93MQ&list=PLuHgQVnccGMAQvSVKdXFiOo51HUD8iQQm&index=7
chrome bookmarked Jinie.sej@gmail.com Kung24/2024-1/디지털세미나1
2)생활코딩 GitHub.com 1-5 < push and pull 기본 원리 << 내 에러코드에 대한 설명은 없음
https://www.youtube.com/watch?v=hjsFW7ry8GA
chrome bookmarked Jinie.sej@gmail.com Kung24/2024-1/디지털세미나1
3)jinie.sej ChGPT 서로 다른 로컬-원격 저장소 이력 병합 허용 < 에러 근본 해결
https://chatgpt.com/share/188be603-932c-4679-910b-969db4126d8a

#### Repository 병합 ( Error-1 git pull and push error)
jinie_porjects 이전 repository에서 발생한 push 문제 (git pull 이후에 git push해도 계속해서 git pull을 먼저하라는 오류)는 다음 코드로 해결.
```vscodeterminal
git pull origin main --allow-unrelated-histories
```


1) error: fatal: refusing to merge unrelated histories 오류
```
PS C:\Users\MSI\Desktop\project> git pull origin main
From https://github.com/JinieFerry/welcome
 * branch            main       -> FETCH_HEAD
fatal: refusing to merge unrelated histories
PS C:\Users\MSI\Desktop\project> git add .
>> git commit -m "version5"
>>
On branch main
nothing to commit, working tree clean
PS C:\Users\MSI\Desktop\project> git push -u origin main
>> 
fatal: unable to connect to cache daemon: Unknown error
To https://github.com/JinieFerry/welcome.git
 ! [rejected]        main -> main (non-fast-forward)
error: failed to push some refs to 'https://github.com/JinieFerry/welcome.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. If you want to integrate the remote changes, 
hint: use 'git pull' before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details. 
PS C:\Users\MSI\Desktop\project>

git remote add origin https://github.com/JinieFerry/jinie_projects.git
git branch -M main
git push -u origin main
```


2) fixer code : 로컬 저장소와 원격 저장소 간에 이력이 서로 다른 경우, 새로운 이력을 생성하고 병합하도록 Git에 명시적으로 지시
```
 git pull origin main --allow-unrelated-histories
```
-> 병합을 허용
