  const { createApp, ref } = Vue

  createApp({
    data() {
      return {
        activeTab: 'transactions',
      }
    }
  }).mount('#kope')