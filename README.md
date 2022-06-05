# todoproject

## 概要
* 登録したToDoを指定した優先度順で管理を行う

## 環境
* Ubuntu
* Python3
* Django3.2
* Bootstrap5.0.2

## デモ
 * ![デモ](https://admin)

## 使用方法
### 新規作成
1. [新規作成]ボタンを押下
2. 必要項目の入力
    1. タイトル
    2. メモ
    3. 優先度(高・中・低)
    4. 期限
3. [作成]ボタンを押下

### 詳細確認
1. [詳細]ボタンを押下
2. 項目の表示
    1. タイトル
    2. メモ
    3. 優先度(高・中・低)
    4. 期限
3. [完了]ボタンを押下

### 編集
2. [編集]ボタンを押下
3. 必要項目の修正
    1. タイトル
    2. メモ
    3. 優先度(高・中・低)
    4. 期限
3. [変更]ボタンを押下

### 削除
1. [削除]ボタンを押下

## 参考資料
* Model Field一覧：https://kuma-server.com/model-field/
* Bootstrupドキュメント:https://getbootstrap.jp/docs/5.0/getting-started/introduction/

## 開発メモ
* アプリ作成：django-admin startapp <アプリ名> .
* migrationファイルの作成：python3 manage.py makemigrations
* DBのテーブル作成：python3 manage.py migrate
* runサーバー実行：python3 manage.py runserver
* djangoユーザーの作成：python3 manage.py createsuperuser

## 課題
   __デザイン(Bootstrup)、今回は機能実装が目的。後日要対応。__
   

![TodeList_01 drawio](https://user-images.githubusercontent.com/106885676/172039984-35c0f40f-aed8-4b2a-bfaf-b12aab8271a5.png)



