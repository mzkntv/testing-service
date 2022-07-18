import axios from 'axios';

export const HTTP = axios.create({
  baseURL: `http://127.0.0.1:5173/`,
})

const requestHandler = (request) => {
  const token = localStorage.getItem('auth_token') || '';
  if (token) {
    request.headers.Authorization = `Token ${token}`;
  }
  return request;
};

const errorHandler = error => {
  return Promise.reject(error);
};

HTTP.interceptors.request.use(
(request) => requestHandler(request),
(error) => errorHandler(error),
);
