// Variáveis globais para os gráficos
let chartVendasTempo, chartVendasCategoria, chartVendasRegiao, chartTopProdutos, chartMargemLucro, chartVendasDiaSemana, chartVendasVendedor;

// Função principal para carregar dashboard
function carregarDashboard() {
    const dataInicio = document.getElementById('dataInicio').value;
    const dataFim = document.getElementById('dataFim').value;
    
    carregarKPIs(dataInicio, dataFim);
    carregarGraficoVendasTempo(dataInicio, dataFim);
    carregarGraficoVendasCategoria(dataInicio, dataFim);
    carregarGraficoVendasRegiao(dataInicio, dataFim);
    carregarGraficoTopProdutos(dataInicio, dataFim);
    carregarGraficoMargemLucro(dataInicio, dataFim);
    carregarGraficoVendasDiaSemana(dataInicio, dataFim);
    carregarGraficoVendasVendedor(dataInicio, dataFim);
    carregarTabelaVendedores(dataInicio, dataFim);
}


// Carrega gráfico de desempenho por vendedor
function carregarGraficoVendasVendedor(dataInicio, dataFim) {
    let url = '/data/vendas-vendedor';

    fetchJson(url, dataInicio, dataFim, 10)
        .then(data => {
            const ctx = document.getElementById('chartVendasVendedor').getContext('2d');

            if (chartVendasVendedor) {
                chartVendasVendedor.destroy();
            }

            chartVendasVendedor = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: data.labels,
                    datasets: [
                        {
                        label: 'Vendas (R$)',
                        data: data.valores,
                        backgroundColor: 'rgba(102, 16, 242, 0.8)'
                    },
                ]
                },
                options: {
                    indexAxis: 'y',
                    responsive: true,
                    plugins: {
                        legend: { display: false },
                        tooltip: {
                            callbacks: {
                                label: function(context) {
                                    const i = context.dataIndex;
                                    const receita = data.valores[i] || 0;
                                    const qtd = data.quantidades?.[i] ?? 0;
                                    const ticket = data.ticket_medio?.[i] ?? 0;
                                    const perc = data.percentual_receita?.[i] ?? 0;
                                    return [
                                        `Receita: ${formatarMoeda(receita)}`,
                                        `Quantidades: ${Number(qtd).toLocaleString('pt-BR')}`,
                                        `Ticket médio: ${formatarMoeda(ticket)}`,
                                        `Participação: ${Number(perc).toFixed(2)}%`
                                    ];
                                }
                            }
                        }
                    },
                    scales: {
                        x: {
                            beginAtZero: true,
                            ticks: {
                                callback: function(value) {
                                    return 'R$ ' + value.toLocaleString('pt-BR');
                                }
                            }
                        }
                    }
                }
            });
        })
        .catch(error => console.error('Erro ao carregar gráfico de vendedores:', error));
}

// B5 simples: tabela de vendedores com filtro de texto
let _vendorsCache = [];
function carregarTabelaVendedores(dataInicio, dataFim) {
    const url = '/data/vendas-vendedor';
    fetchJson(url, dataInicio, dataFim, 50)
        .then(data => {
            _vendorsCache = (data.labels || []).map((v, i) => ({
                ranking: (data.ranking && data.ranking[i]) || (i + 1),
                vendedor: v,
                valores: data.valores?.[i] || 0,
                quantidades: data.quantidades?.[i] || 0,
                ticket_medio: data.ticket_medio?.[i] || 0,
                percentual_receita: data.percentual_receita?.[i] || 0
            }));
            renderTabelaVendedores(_vendorsCache);
            wireFiltroVendedores();
        })
        .catch(err => console.error('Erro ao carregar tabela de vendedores:', err));
}

function renderTabelaVendedores(rows) {
    const tbody = document.querySelector('#tableVendedores tbody');
    if (!tbody) return;
    const fmtNum = n => Number(n).toLocaleString('pt-BR');
    const fmtMoeda = n => formatarMoeda(n);
    tbody.innerHTML = rows.map(r => `
        <tr>
            <td>${r.ranking}</td>
            <td>${r.vendedor}</td>
            <td>${fmtMoeda(r.valores)}</td>
            <td>${fmtNum(r.quantidades)}</td>
            <td>${fmtMoeda(r.ticket_medio)}</td>
            <td>${Number(r.percentual_receita).toFixed(2)}%</td>
        </tr>
    `).join('');
}

function wireFiltroVendedores() {
    const input = document.getElementById('vendorSearch');
    if (!input || input._wired) return;
    input.addEventListener('input', (e) => {
        const q = (e.target.value || '').toLowerCase();
        const filtradas = q ? _vendorsCache.filter(r => r.vendedor.toLowerCase().includes(q)) : _vendorsCache;
        renderTabelaVendedores(filtradas);
    });
    input._wired = true;
}

// Carrega KPIs
function carregarKPIs(dataInicio, dataFim) {
    let url = '/data/kpis';
    url = buildUrl(url, dataInicio, dataFim);
    fetch(url)
        .then(response => response.json())
        .then(data => {
            document.getElementById('kpiReceitaTotal').textContent = 
                formatarMoeda(data.receita_total);
            document.getElementById('kpiNumVendas').textContent = 
                formatarNumero(data.num_vendas);
            document.getElementById('kpiTicketMedio').textContent = 
                formatarMoeda(data.ticket_medio);
        })
        .catch(error => console.error('Erro ao carregar KPIs:', error));
}

// Carrega gráfico de vendas ao longo do tempo
function carregarGraficoVendasTempo(dataInicio, dataFim) {
    let url = '/data/vendas-tempo';
    
    fetchJson(url, dataInicio, dataFim)
        .then(data => {
            const ctx = document.getElementById('chartVendasTempo').getContext('2d');
            
            if (chartVendasTempo) {
                chartVendasTempo.destroy();
            }
            
            chartVendasTempo = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: data.labels,
                    datasets: [
                        {
                            label: 'Valor (R$)',
                            data: data.valores,
                            borderColor: 'rgb(13, 110, 253)',
                            backgroundColor: 'rgba(13, 110, 253, 0.1)',
                            tension: 0.3,
                            pointRadius: 0
                        },
                        {
                            label: 'Média Móvel 7d',
                            data: data.media_movel_7,
                            borderColor: 'rgba(25, 135, 84, 0.9)',
                            backgroundColor: 'transparent',
                            borderWidth: 2,
                            tension: 0.2,
                            pointRadius: 0
                        },
                        {
                            label: 'Média Móvel 30d',
                            data: data.media_movel_30,
                            borderColor: 'rgba(255, 193, 7, 0.9)',
                            backgroundColor: 'transparent',
                            borderWidth: 2,
                            tension: 0.2,
                            pointRadius: 0
                        }
                    ]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: true,
                    plugins: {
                        legend: {
                            display: true,
                            position: 'top'
                        }
                    },
                    scales: {
                        y: {
                            beginAtZero: true,
                            ticks: {
                                callback: function(value) {
                                    return 'R$ ' + value.toLocaleString('pt-BR');
                                }
                            }
                        }
                    }
                }
            });
        })
        .catch(error => console.error('Erro ao carregar gráfico:', error));
}

// Carrega gráfico de vendas por categoria
function carregarGraficoVendasCategoria(dataInicio, dataFim) {
    let url = '/data/vendas-categoria';
    
    fetchJson(url, dataInicio, dataFim)
        .then(data => {
            const ctx = document.getElementById('chartVendasCategoria').getContext('2d');
            
            if (chartVendasCategoria) {
                chartVendasCategoria.destroy();
            }
            
            chartVendasCategoria = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: data.labels,
                    datasets: [{
                        label: 'Vendas (R$)',
                        data: data.valores,
                        backgroundColor: [
                            'rgba(13, 110, 253, 0.8)',
                            'rgba(25, 135, 84, 0.8)',
                            'rgba(255, 193, 7, 0.8)',
                            'rgba(220, 53, 69, 0.8)',
                            'rgba(13, 202, 240, 0.8)'
                        ]
                    }]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: {
                            display: false
                        }
                    },
                    scales: {
                        y: {
                            beginAtZero: true,
                            ticks: {
                                callback: function(value) {
                                    return 'R$ ' + value.toLocaleString('pt-BR');
                                }
                            }
                        }
                    }
                }
            });
        })
        .catch(error => console.error('Erro ao carregar gráfico:', error));
}

// Carrega gráfico de vendas por região
function carregarGraficoVendasRegiao(dataInicio, dataFim) {
    let url = '/data/vendas-regiao';
    
    fetchJson(url, dataInicio, dataFim)
        .then(data => {
            const ctx = document.getElementById('chartVendasRegiao').getContext('2d');
            
            if (chartVendasRegiao) {
                chartVendasRegiao.destroy();
            }
            
            chartVendasRegiao = new Chart(ctx, {
                type: 'pie',
                data: {
                    labels: data.labels,
                    datasets: [{
                        data: data.valores,
                        backgroundColor: [
                            'rgba(13, 110, 253, 0.8)',
                            'rgba(25, 135, 84, 0.8)',
                            'rgba(255, 193, 7, 0.8)',
                            'rgba(220, 53, 69, 0.8)',
                            'rgba(13, 202, 240, 0.8)'
                        ]
                    }]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: {
                            position: 'bottom'
                        },
                        tooltip: {
                            callbacks: {
                                label: function(context) {
                                    const label = context.label || '';
                                    const value = formatarMoeda(context.parsed);
                                    const percentual = data.percentuais[context.dataIndex];
                                    return `${label}: ${value} (${percentual}%)`;
                                }
                            }
                        }
                    }
                }
            });
        })
        .catch(error => console.error('Erro ao carregar gráfico:', error));
}

// Carrega gráfico de top produtos
function carregarGraficoTopProdutos(dataInicio, dataFim) {
    let url = '/data/top-produtos';
    
    fetchJson(url, dataInicio, dataFim, 10)
        .then(data => {
            const ctx = document.getElementById('chartTopProdutos').getContext('2d');
            
            if (chartTopProdutos) {
                chartTopProdutos.destroy();
            }
            
            chartTopProdutos = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: data.labels,
                    datasets: [{
                        label: 'Vendas (R$)',
                        data: data.valores,
                        backgroundColor: 'rgba(25, 135, 84, 0.8)'
                    }]
                },
                options: {
                    indexAxis: 'y',
                    responsive: true,
                    plugins: {
                        legend: {
                            display: false
                        }
                    },
                    scales: {
                        x: {
                            beginAtZero: true,
                            ticks: {
                                callback: function(value) {
                                    return 'R$ ' + value.toLocaleString('pt-BR');
                                }
                            }
                        }
                    }
                }
            });
        })
        .catch(error => console.error('Erro ao carregar gráfico:', error));
}

// Carrega gráfico de margem de lucro
function carregarGraficoMargemLucro(dataInicio, dataFim) {
    let url = '/data/vendas-margem-lucro';

    fetchJson(url, dataInicio, dataFim)
        .then(data => {
            const ctx = document.getElementById('chartMargemLucro').getContext('2d');

            if (chartMargemLucro) {
                chartMargemLucro.destroy();
            }

            chartMargemLucro = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: data.labels,
                    datasets: [{
                        label: 'Margem de Lucro (%)',
                        data: data.margem,
                        backgroundColor: 'rgba(54, 162, 235, 0.7)'
                    }]
                },
                options: {
                    indexAxis: 'y',
                    responsive: true,
                    plugins: {
                        legend: { display: false },
                        tooltip: {
                            callbacks: {
                                label: function(context) {
                                    const i = context.dataIndex;
                                    const lucro = data.lucro[i] || 0;
                                    const receita = data.receita[i] || 0;
                                    const margem = data.margem[i] || 0;
                                    return [
                                        `Lucro: R$ ${lucro.toLocaleString('pt-BR')}`,
                                        `Receita: R$ ${receita.toLocaleString('pt-BR')}`,
                                        `Margem: ${Number(margem).toFixed(2)}%`
                                    ];
                                }
                            }
                        }
                    },
                    scales: {
                        x: {
                            beginAtZero: true,
                            max: 100,
                            ticks: {
                                callback: function(value) { return value + '%' }
                            },
                            title: { display: true, text: 'Margem (%)' }
                        }
                    }
                }
            });
        })
        .catch(error => console.error('Erro ao carregar gráfico:', error));
}

function carregarGraficoVendasDiaSemana(dataInicio, dataFim) {
    let url = '/data/vendas-dia-semana';

    fetchJson(url, dataInicio, dataFim)
        .then(data => {
            const ctx = document.getElementById('chartVendasDiaSemana').getContext('2d');
            
            if (chartVendasDiaSemana) {
                chartVendasDiaSemana.destroy();
            }
            
            chartVendasDiaSemana = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: data.labels,
                    datasets: [
                        {
                            label: 'Vendas (R$)',
                            data: data.valores,
                            backgroundColor: 'rgba(13, 110, 253, 0.8)',
                            yAxisID: 'yValor'
                        },
                        {
                            label: 'Quantidades',
                            data: data.quantidades,
                            backgroundColor: 'rgba(25, 135, 84, 0.7)',
                            yAxisID: 'yQtd'
                        }
                    ]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: { display: true },
                        tooltip: {
                            callbacks: {
                                label: function(context) {
                                    if (context.dataset.yAxisID === 'yValor') {
                                        return `${context.dataset.label}: ${formatarMoeda(context.parsed.y ?? context.parsed)}`;
                                    }
                                    const v = context.parsed.y ?? context.parsed;
                                    return `${context.dataset.label}: ${Number(v).toLocaleString('pt-BR')}`;
                                }
                            }
                        }
                    },
                    scales: {
                        yValor: {
                            type: 'linear',
                            position: 'left',
                            beginAtZero: true,
                            ticks: {
                                callback: function(value) { return 'R$ ' + value.toLocaleString('pt-BR'); }
                            },
                            title: { display: true, text: 'Vendas (R$)' }
                        },
                        yQtd: {
                            type: 'linear',
                            position: 'right',
                            beginAtZero: true,
                            grid: { drawOnChartArea: false },
                            ticks: {
                                callback: function(value) { return value.toLocaleString('pt-BR'); }
                            },
                            title: { display: true, text: 'Quantidades' }
                        },
                        x: {
                            title: { display: true, text: 'Dia da Semana' }
                        }
                    }
                }
            });
        })
        .catch(error => console.error('Erro ao carregar gráfico:', error));
}


function buildUrl(url, dataInicio, dataFim) {
    const params = new URLSearchParams();
    if (dataInicio) params.append('data_inicio', dataInicio);
    if (dataFim) params.append('data_fim', dataFim);
    if (params.toString()) url += '?' + params.toString();
    return url;
}

function buildUrlWithLimit(url, dataInicio, dataFim, limite) {
    url += `?limite=${limite}`;
    const params = new URLSearchParams();
    if (dataInicio) params.append('data_inicio', dataInicio);
    if (dataFim) params.append('data_fim', dataFim);
    url += '&' + params.toString();
    return url
}
    

// Helper: fetch JSON com montagem de URL e tratamento básico de erro HTTP
function fetchJson(url, dataInicio, dataFim, limite=0) {
    if (limite) {
        url = buildUrlWithLimit(url, dataInicio, dataFim, limite);
    } else {
        url = buildUrl(url, dataInicio, dataFim);
    }
    return fetch(url).then(resp => {
        if (!resp.ok) {
            throw new Error(`HTTP ${resp.status} em ${url}`);
        }
        return resp.json();
    });
}

// Event listeners
document.getElementById('aplicarFiltros').addEventListener('click', function() {
    carregarDashboard();
});

document.getElementById('limparFiltros').addEventListener('click', function() {
    document.getElementById('dataInicio').value = '';
    document.getElementById('dataFim').value = '';
    carregarDashboard();
});

// Upload de arquivo
document.getElementById('uploadButton').addEventListener('click', function() {
    const form = document.getElementById('uploadForm');
    const formData = new FormData(form);
    
    fetch('/api/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert('Erro: ' + data.error);
        } else {
            alert('Arquivo processado com sucesso! ' + data.registros + ' registros importados.');
            bootstrap.Modal.getInstance(document.getElementById('uploadModal')).hide();
            form.reset();
            carregarDashboard();
        }
    })
    .catch(error => {
        alert('Erro ao fazer upload: ' + error);
    });
});

// Funções auxiliares
function formatarMoeda(valor) {
    return new Intl.NumberFormat('pt-BR', {
        style: 'currency',
        currency: 'BRL'
    }).format(valor);
}

function formatarNumero(valor) {
    return new Intl.NumberFormat('pt-BR').format(valor);
}

// B5: ordenação DOM-only na tabela de vendedores
document.addEventListener('DOMContentLoaded', function() {
    const thead = document.querySelector('#tableVendedores thead');
    const tbody = document.querySelector('#tableVendedores tbody');
    if (!thead || !tbody) return;
    thead.addEventListener('click', (ev) => {
        const th = ev.target.closest('th[data-sort]');
        if (!th) return;
        const colIndex = parseInt(th.getAttribute('data-sort'), 10);
        const currentDir = th.getAttribute('data-dir') === 'asc' ? 'asc' : 'desc';
        const newDir = currentDir === 'asc' ? 'desc' : 'asc';
        th.setAttribute('data-dir', newDir);

        const rows = Array.from(tbody.querySelectorAll('tr'));
        const normalize = (txt) => {
            if (txt == null) return '';
            const s = String(txt).trim()
                .replace(/^R\$\s*/,'')
                .replace(/\.%/g,'')
                .replace(/%/g,'')
                .replace(/\./g,'')
                .replace(/,/g,'.');
            const num = Number(s);
            return isNaN(num) ? txt.toLowerCase() : num;
        };
        rows.sort((a, b) => {
            const aTxt = a.children[colIndex]?.textContent || '';
            const bTxt = b.children[colIndex]?.textContent || '';
            const av = normalize(aTxt);
            const bv = normalize(bTxt);
            let cmp;
            if (typeof av === 'number' && typeof bv === 'number') {
                cmp = av - bv;
            } else {
                cmp = String(av).localeCompare(String(bv), 'pt-BR', { sensitivity: 'base' });
            }
            return newDir === 'asc' ? cmp : -cmp;
        });
        // Reanexar linhas ordenadas
        rows.forEach(tr => tbody.appendChild(tr));
    });
});

