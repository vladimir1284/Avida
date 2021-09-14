import { writable } from 'svelte/store';

export const clients = writable({});
export const orders = writable({});
export const base_url = "http://localhost:8000/fb_avida/"