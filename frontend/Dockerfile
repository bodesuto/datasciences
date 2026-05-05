# Giai đoạn Build: Biên dịch mã nguồn React
FROM node:18-alpine as build-stage

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build

# Giai đoạn Production: Sử dụng Nginx để phục vụ file tĩnh
FROM nginx:stable-alpine as production-stage

# Copy file đã build vào thư mục của Nginx
COPY --from=build-stage /app/dist /usr/share/nginx/html

# Mở cổng 80 cho web
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
