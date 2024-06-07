# yakiniku-api

## 使用方法

### 準備

- gitをクローン

https
```
git clone https://github.com/yakiniku-hackathon/yakiniku-api.git
```
ssh
```
git clone git@github.com:yakiniku-hackathon/yakiniku-api.git
```
- 一つ下のディレクトリに移動
```
cd yakiniku-api
```

### dockerの起動

- dockerの起動
```
docker compose up -d
```
※不調の場合は以下のコマンドを順番に実行
```
docker compose donw
docker compose up -d
```

- dockerの停止
```
docker compose down
```

- dockerの完全削除
```
docker compose down --rmi all -v
```