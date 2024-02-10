  const { createApp, ref } = Vue

  createApp({
    data() {
      return {
        activeTab: 'transactions',
      }
    },
    methods: {
      openPopup() {
        this.isPopupOpen = true;
      },
      closePopup() {
        this.isPopupOpen = false;
      },
    },
  
  }).mount('#kope')