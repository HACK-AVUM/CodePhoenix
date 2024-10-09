import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    host: '0.0.0.0', // Allow access from the outside
    port: 3000,
    https: true, // Use HTTPS
    hmr: {
      protocol: 'wss', // Use WebSocket Secure
      host: 'codephoenix.italynorth.cloudapp.azure.com', // Set the correct host
    },
  },
});
