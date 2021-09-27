import { INavData } from '@coreui/angular';

export const navItems: INavData[] = [
  {
    name: 'Página Principal',
    url: '/dashboard',
    icon: 'icon-speedometer',
    // badge: {
    //   variant: 'info',
    //   text: 'NEW'
    // }
  },
  {
    title: true,
    name: 'Opciones de Sistema'
  },
  {
    name: 'Administración',
    url: '/base',
    icon: 'icon-home',
    children: [
      {
        name: 'Clientes',
        url: '/base/customers',
        icon: 'icon-people'
      },
      {
        name: 'Prospectos',
        url: '/base/leads',
        icon: 'icon-puzzle'
      }
    ]
  }
];
