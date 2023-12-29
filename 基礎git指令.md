# git 簡易說明

[Git 練習場](https://gitbook.tw/playground)
[Git 教學(工具書)](https://nulab.com/zh-tw/learn/software-development/git-tutorial/)

git 是一個版本控制（**版控**）的軟體，它的特色在於可以在不同地點同時進行開發作業  
一份原始碼庫我們稱之為 repository，簡稱會是 **repo**，**儲存庫**  
repo 本身有**本地端**與**遠端**  最大的遠端 repo 是 GitHub
git 本身是由 commit（提交紀錄） 與 branch（分支）組成，用來追蹤目前原始碼的版本  
  - 提交檔案的時候 **一定要** 提供訊息
git 的檔案有幾個階段
- untracked: 檔案沒有被 git 追蹤變更
- new file: 檔案被加入版控
- Modified：檔案有被 git 追蹤，並且被發現修改
- staged：準備提交階段
- commit：提交紀錄

## 安裝 git

- [Git 官網](https://git-scm.com/download/win)

## Git 基本指令

1. 複製一份原始碼到本機
  - git clone https://github.com/jg40305/template_code.git
2. 查看目前 git 狀態（哪些檔案） 
  - git status

  ```shell
  Changes to be committed:
    以下為這次變更會被記錄的檔案
    new file:   "\345\237\272\347\244\216git\346\214\207\344\273\244.md"
  Untracked files:
    以下為沒有被 git 追蹤的檔案
  ```
2. 將變更的檔案進入下一個 stage
  - git add <檔案名稱>
    - git add . => (將所有的變更加入)
  - **注意** 不要將超過 100MB 的檔案 add 進來
3. git commit -m "提交訊息"：將這次的變更紀錄提交，通常是說明這次做什麼事情，執行了什麼任務
4. git pull：拉取遠端 repo 的變更
5. git push：將變更推送至遠端 repo
  - 第一次通常會先使用 git push -u origin master
    - 說文解字：
      - git push: 推送指令
      - -u：追蹤遠端變更（只需輸入一次）
      - origin：遠端的名稱，可以輸入 git remote show origin 查看
      - master：分支名稱（須注意最近 github 預設會使用 main）
